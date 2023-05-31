import asyncio
# import datetime
# import logging
# from model.balance_CQG import BalanceCQGModel
import nest_asyncio
from flask_restful import Resource

from CQG_balance_setup import balance_request_setup
from development_config import Config

_use_case_map = {
    'balance_request_setup': balance_request_setup,
}


class CmsApi(Resource):
    @classmethod
    def get(cls):
        # logging.basicConfig(
        #     filename=f'./logs/account_setup--{datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")}.log',
        #     filemode='w', encoding='utf-8', level=logging.DEBUG)
        config = Config()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(asyncio.new_event_loop())
        nest_asyncio.apply()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(_use_case_map['balance_request_setup'].run(config))
        return "ok"
