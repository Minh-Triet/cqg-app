import logging
import time

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger
from pytz import timezone

from development_config import SQLALCHEMY_DATABASE_URI

jobstores = {
    'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)  # 会自动在当前目录创建该sqlite文件
}

executors = {
    'default': ThreadPoolExecutor(max_workers=1)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 2
}
# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)


def add():
    for a in range(5):
        time.sleep(1)
        logger.debug(a)


def abc():
    x = 9
    y = 3.0
    print(True and False)


def acb():
    logger.debug('job3')


scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults,
                                timezone=timezone('Asia/Shanghai'))

scheduler.add_job(add, 'interval', seconds=2, id='1', replace_existing=True)
# scheduler.add_job(abc, 'interval', seconds=6, id='3', replace_existing=True)
# scheduler.add_job(acb, 'interval', seconds=7, id='4', replace_existing=True)
scheduler.start()
# scheduler.remove_all_jobs()
try:
    while True:
        time.sleep(20)
        print('Delay 2s')
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()  # wait=False参数可选，代表立即停止，不用等待。
    print('Scheduler failed to start')
