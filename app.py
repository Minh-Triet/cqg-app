import datetime

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from loguru import logger

from ma import ma, db
from resources.balance_CQG import CmsApi
from resources.number import NumberTest
from resources.trade_cqg import TradeCQG

app = Flask(__name__)

load_dotenv('.env')
app.config.from_object('development_config')  # load default configs from development_config.py
app.config.from_envvar('APPLICATION_SETTINGS')  # override with config.py (APPLICATION_SETTINGS points to config.py)
# logger.add(f'logs/{datetime.datetime.now().strftime("%Y-%m-%d")}.log', level='DEBUG', rotation='00:00')
api = Api(app)
migrate = Migrate(app, db)
db.init_app(app)

api.add_resource(TradeCQG, '/cqg')
api.add_resource(NumberTest, '/test')
api.add_resource(CmsApi, '/balance_cqg')

import socket


# Function to display hostname and
# IP address


def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        logger.debug("Hostname :  ", host_name)
        logger.debug("IP : ", host_ip)
    except:
        logger.debug("Unable to get Hostname and IP")


# Driver code
get_Host_name_IP()  # Function call

if __name__ == '__main__':
    ma.ma.init_app(app)

    app.run(debug=True, host='0.0.0.0', use_reloader=False)
