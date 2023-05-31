import datetime
import json
import logging
import os
import random
import time

from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED  # 调度器时间类型
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.base import JobLookupError
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
# 三种类型的触发器
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger
from pytz import timezone

from development_config import SQLALCHEMY_DATABASE_URI

"""
使用SQLAlchemyJobStore，需要pip install sqlalchemy，否则会提示ImportError: SQLAlchemyJobStore requires SQLAlchemy installed

"""

# 通过logging模块，可以添加apscheduler日志至DEBUG级别，这样就能捕获异常信息，format参数为格式化输出，datefmt为日志日期时间格式
logging.basicConfig(filename='scheduled_run.log', level=logging.DEBUG, format='%(asctime)s|%(levelname)s|%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

jobstores = {
    'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)  # 会自动在当前目录创建该sqlite文件
}

executors = {
    'default': ThreadPoolExecutor(max_workers=20)  # 派生线程的最大数目
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults,
                                timezone=timezone('Asia/Shanghai'))
# scheduler = BlockingScheduler()
scheduler.start()


# 调度器允许添加事件侦听器。作业出错或运行完成时通知
def job_run_listener(event):
    print(event.job_id, event.scheduled_run_time)
    job_id = event.job_id
    scheduled_run_time = event.scheduled_run_time.strftime("%Y-%m-%d %H:%M:%S")
    if event.exception:
        print(
            '作业ID：{} 在 {} 执行失败 :(      错误原因：{}'.format(job_id, scheduled_run_time, event.exception.args[0]))
    else:
        print('作业ID：{} 在 {} 执行成功 :)'.format(job_id, scheduled_run_time))


# 当任务执行完或任务出错时，调用job_run_listener
scheduler.add_listener(job_run_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


def job_schedule_reminder(msg):
    """
    定时通知
    :param msg: 消息内容
    :return:
    """
    with open('schedule.log', 'a', encoding='utf-8') as f:
        f.write('{} 执行任务：{}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg))
        f.close()
    print('系统通知：', msg)


class ScheduleManage(object):
    def __init__(self, sch):
        self.sch = sch

    # 暂停作业
    def pause_job(self, job_id, jobstore=None):
        self.sch.pause_job(job_id, jobstore=jobstore)
        msg = '作业ID：{} 暂停成功'.format(job_id)
        print(msg)

    # 恢复作业
    def resume_job(self, job_id, jobstore=None):
        self.sch.resume_job(job_id, jobstore=jobstore)
        msg = '作业ID：{} 恢复成功'.format(job_id)
        print(msg)

    # 删除作业
    def remove_job(self, job_id=None, jobstore=None):
        if job_id is None:
            if input('确认删除所有作业？') == 'y':
                self.sch.remove_all_jobs(jobstore=jobstore)
            msg = '所有作业删除成功'
        else:
            try:
                self.sch.remove_job(job_id, jobstore=jobstore)
                msg = '作业ID：{} 删除成功'.format(job_id)
            except JobLookupError as e:
                msg = '作业ID不存在：{}'.format(e)
        print(msg)

    # 获取作业的触发器和配置的时间字符串，以及作业下次运行时间等信息
    def get_job(self, job_id, jobstore=None):
        """
        获取作业的所有信息
        :param job_id: 作业ID
        :param jobstore:
        :return: id、name、func、func_args、func_kwargs、trigger、trigger_time、state、next_run_time
        """
        job = self.sch.get_job(job_id, jobstore)

        job_info = dict()
        job_info['id'] = job.id
        job_info['name'] = job.name
        job_info['func'] = job.func.__name__
        job_info['func_args'] = job.args
        job_info['func_kwargs'] = job.kwargs

        if isinstance(job.trigger, DateTrigger):
            job_info['trigger'] = 'date'
            job_info['trigger_time'] = job.trigger.run_date.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(job.trigger, IntervalTrigger):
            job_info['trigger'] = 'interval'
            # print(job.trigger.interval.days)
            w, d = divmod(job.trigger.interval.days, 7)  # 天转换为周、天
            # print(job.trigger.interval.seconds)
            m, s = divmod(job.trigger.interval.seconds, 60)  # 秒转换为时、分、秒
            h, m = divmod(m, 60)
            job_info['trigger_time'] = '{} {} {} {} {}'.format(s, m, h, d, w)
        elif isinstance(job.trigger, CronTrigger):
            job_info['trigger'] = 'cron'
            job_info['trigger_time'] = '{} {} {} {} {} {} {}'.format(job.trigger.fields[7],
                                                                     job.trigger.fields[6],
                                                                     job.trigger.fields[5],
                                                                     job.trigger.fields[4],
                                                                     job.trigger.fields[3],
                                                                     job.trigger.fields[2],
                                                                     job.trigger.fields[1])
        else:
            job_info['trigger'] = job_info['trigger_time'] = None
        next_run_time = job.next_run_time
        if next_run_time:
            # 作业运行中
            job_info['state'] = '运行中'
            job_info['next_run_time'] = next_run_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            # 作业暂停中，next_run_time为None，进行获取
            job_info['state'] = '暂停中'
            job_info['next_run_time'] = '{}(恢复运行后)'.format(
                job.trigger.get_next_fire_time(None, datetime.datetime.now(timezone('Asia/Shanghai'))).strftime(
                    "%Y-%m-%d %H:%M:%S"))
        print(job_info)
        return job_info

    # 获取所有作业
    def get_jobs(self):
        all_jobs = self.sch.get_jobs()
        job_infos = []
        for job in all_jobs:
            job_infos.append(self.get_job(job.id))
        return json.dumps(job_infos)

    # 处理add、modify传入的kwargs
    @staticmethod
    def run_trigger_time(trigger, trigger_time, start_end_date):
        kwargs = {}
        if trigger == 'date':
            kwargs['run_date'] = trigger_time
        elif trigger == 'interval':
            """
            :param int weeks: number of weeks to wait
            :param int days: number of days to wait
            :param int hours: number of hours to wait
            :param int minutes: number of minutes to wait
            :param int seconds: number of seconds to wait
            """
            kwargs['seconds'], kwargs['minutes'], kwargs['hours'], kwargs['days'], kwargs['weeks'] = map(int,
                                                                                                         trigger_time.split(
                                                                                                             ' '))
            kwargs.update(start_end_date)  # 添加起止日期
        elif trigger == 'cron':
            """
            :param int|str year: 4-digit year
            :param int|str month: month (1-12)
            :param int|str day: day of the (1-31)
            :param int|str day_of_week: number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
            :param int|str hour: hour (0-23)
            :param int|str minute: minute (0-59)
            :param int|str second: second (0-59)
            """
            kwargs['second'], kwargs['minute'], kwargs['hour'], kwargs['day'], kwargs['month'], kwargs['day_of_week'], \
                kwargs['year'] = trigger_time.split(' ')
            kwargs.update(start_end_date)  # 添加起止日期
        else:
            pass
        return kwargs

    # 添加作业
    def add_job(self, func, trigger, trigger_time, func_args=None, func_kwargs=None, jobstore='default', **kwargs):
        """
        date:
            .add_job(job_function, 'date', args=['msg'], run_date='2020-02-20 12:12:00')
        interval:
            .add_job(job_function, 'interval', hours=2, start_date='2020-02-20 12:12:00', end_date='2020-02-22 12:12:00')
        cron:
            .add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
        :param func: 执行的函数名
        :param trigger: 触发器类型：date、interval、cron
        :param trigger_time: 执行时间信息：
                            date->'2020-02-20 12:12:00'
                            interval->'秒 分 时 日 周'：每2s（2 0 0 0 0），每1天12小时（0 0 12 1 0），每1周（0 0 0 0 1）
                            cron->'秒 分 时 日 月 周 年'：每日xx:xx:00（0 x x * * * *）、每周x（0 x x * * x *）、每月x日（0 x x x * * *）、每年x月x日（0 x x x x * *）
        :param func_args: 要调用func的位置参数list
        :param func_kwargs: 调用func的关键字参数dict
        :param jobstore: 存储器，默认
        :return: job_id
        """
        random_num = random.randint(100, 999)
        job_id = '{}_{}_{}'.format(trigger, int(time.time()), random_num)  # 时间戳+随机数为id
        job_name = '{}_{}'.format(func.__name__, random_num)

        start_end_date = {'start_date': kwargs.get('start_date', None),
                          'end_date': kwargs.get('end_date', None)}  # interval和cron可能传入的起止日期

        add_kwargs = {'func': func, 'trigger': trigger, 'args': func_args, 'kwargs': func_kwargs, 'id': job_id,
                      'name': job_name}  # 指定添加作业的参数
        add_kwargs.update(
            self.run_trigger_time(trigger=trigger, trigger_time=trigger_time, start_end_date=start_end_date))  # 将时间参数合并

        # print(add_kwargs)
        if trigger in ('date', 'interval', 'cron'):
            try:
                job = self.sch.add_job(**add_kwargs)
                print('当前新建任务：', job)
                # 获取当前创建作业的下次运行时间
                # next_run_time = scheduler.get_job(job_id).next_run_time
                next_run_time = job.next_run_time  # <class 'datetime.datetime'>offset-aware类型，包含时区的
                next_run_time = next_run_time.replace(
                    tzinfo=None)  # offset-aware类型的datetime转换为offset-naive类型的datetime，即去掉时间戳

                now_datetime = datetime.datetime.now()  # 获取当前时间
                if next_run_time <= now_datetime:
                    print('The task time must be greater than the current time, the task has been automatically deleted by the system, and the creation failed！')
                else:
                    week = {
                        '0': '日',
                        '1': '一',
                        '2': '二',
                        '3': '三',
                        '4': '四',
                        '5': '五',
                        '6': '六',
                    }
                    print('定时任务创建成功，job_id：{}，下次运行时间：{}（周{}）'.format(job_id, next_run_time,
                                                                                    week[next_run_time.strftime('%w')]))
            except ValueError as e:
                print('异常：', e)
            return job_id
        else:
            print('Creation failed, specified trigger error')
            return None


sch = ScheduleManage(scheduler)
sch.get_jobs()
# sch.pause_job('interval_1582123807_794')
# job_id = sch.add_job(func=job_schedule_reminder, trigger='date', trigger_time='2020-2-20 21:00:00', func_args=['date：今天晚上8:00部门开会'])
#
job_id = sch.add_job(func=job_schedule_reminder, trigger='interval', trigger_time='2 0 0 0 0',
                     func_args=['interval：every 2s send a notice'])  # 每隔xx时间
# job_id = sch.add_job(func=job_schedule_reminder, trigger='interval', trigger_time='0 0 12 1 0', func_args=['interval：每隔1天12小时发个通知'])  # 每隔xx时间
# job_id = sch.add_job(func=job_schedule_reminder, trigger='interval', trigger_time='1 0 12 0 1', func_args=['interval：每隔1周12小时1秒发个通知'])  # 每隔xx时间
# job_id = sch.add_job(func=job_schedule_reminder, trigger='interval', trigger_time='1 0 1 1 1', func_args=['interval：每隔1周1天1小时1秒发个通知'])  # 每隔xx时间
#
# job_id = sch.add_job(func=job_schedule_reminder, trigger='cron', trigger_time='0 55 20 * * * *', func_args=['cron：每天20:55定时消息'])
# job_id = sch.add_job(func=job_schedule_reminder, trigger='cron', trigger_time='0 0 12 * * 0,2,4 *', func_args=['cron：每周日、三、五 12:00定时消息'])
# job_id = sch.add_job(func=job_schedule_reminder, trigger='cron', trigger_time='0 0 18 1 * * *', func_args=['cron：每月1号 18:00定时消息'])
# job_id = sch.add_job(func=job_schedule_reminder, trigger='cron', trigger_time='0 30 9 10 12 * *', func_args=['cron：每年12月10日 9:30定时消息'])
time.sleep(10)
sch.remove_job(job_id)

print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
try:
    while True:
        time.sleep(20)
        print('Delay 2s')
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()  # wait=False参数可选，代表立即停止，不用等待。
    print('Scheduler failed to start')
