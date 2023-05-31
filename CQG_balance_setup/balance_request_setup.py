"""Demonstrates how trading account can be set up via CMS API.
[demo] indicates that this step does not make much sense in real use case.
"""
import json
import logging

import pandas as pandas
from loguru import logger

import client_balance_CQG.proto.CMS.traderouting_1_pb2 as traderouting
from client_balance_CQG.cmsapi_client import CmsApiClient
from .common import *

# Random number that is used as value when setting limits.

async def run(config: Config):
    logger.debug("account_setup started...")
    client = CmsApiClient()
    await client.connect(config.cms_api_url)

    logging.info("LOGON")
    await client.send_logon(
        config.username, config.password, config.client_app_id, config.private_label, config.client_version)

    # create balance record

    # account_balance = traderouting.TradeRoutingRequest()
    # balance = account_balance.account_scope_request
    # acc = balance.create_balance_record
    # acc.account_id = 17093758
    # acc.currency = 'VND'
    # acc.end_cash_balance = 0
    # balance_record = await client_balance_CQG.send_traderouting_request(account_balance)
    # logger.debug(balance_record)

    # update balance record

    # account_balance = traderouting.TradeRoutingRequest()
    # balance = account_balance.account_scope_request
    # acc = balance.update_balance_record
    # acc.balance_id = 343490575
    # acc.end_cash_balance = 999999
    # balance_record = await client.send_traderouting_request(account_balance)
    # logger.debug(balance_record)

    account_balance = traderouting.TradeRoutingRequest()
    balance = account_balance.account_scope_request
    acc = balance.balance_records_request
    # acc.balance_id = 321009136
    acc.currency = 'VND'
    acc.account_id = 17093758
    balance_records = await client.send_traderouting_request(account_balance)
    logger.debug(balance_records)

    # account_service = AccountService(client)
    # profile = ProfileService(client)
    # profile_ = await profile.profile_request('C16891391')
    # account = await account_service.account_info_request('17093758')
    # logger.debug(account)
    # logger.debug(profile_)
    balance_record_id = get_balance(balance_records)
    logger.debug(balance_record_id[1])
    # account_balance = traderouting.TradeRoutingRequest()
    # balance = account_balance.account_scope_request
    # acc = balance.update_balance_record
    # acc.balance_id = balance_record_id
    # acc.end_cash_balance = 1234321
    # balance_record = await client.send_traderouting_request(account_balance)
    # logger.debug(balance_record)
    #
    # account_balance = traderouting.TradeRoutingRequest()
    # balance = account_balance.account_scope_request
    # acc = balance.balance_records_request
    # acc.balance_id = balance_record_id
    # # acc.currency = 'VND'
    # # acc.account_id = 17093758
    # balance_records = await client.send_traderouting_request(account_balance)
    # logger.debug(balance_records)
    # あなた
    await client.disconnect()
    logger.debug("account_setup finished.")


def get_balance(balance_records):
    # Get balance with balance_records ID
    from google.protobuf.json_format import MessageToJson
    json_str = MessageToJson(balance_records)
    logger.debug(json_str)
    json_dct = json.loads(json_str)
    account_id = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0]['accountId']
    balance_record_id = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0][
        'balanceRecordId']
    end_cash_balance = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0]['currency']
    currency = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0]['endCashBalance']
    collateral = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0]['collateral']
    time_ms = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0]['asOfDate']
    as_of_date = pandas.to_datetime(time_ms, unit='ms')
    origin = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0]['origin']
    regulated = json_dct['accountScopeResult']['balanceRecordsResult']['balanceRecord'][0]['regulated']

    logger.debug(account_id)
    logger.debug(balance_record_id)
    logger.debug(end_cash_balance)
    logger.debug(currency)
    logger.debug(collateral)
    logger.debug(as_of_date)
    logger.debug(origin)
    logger.debug(regulated)

    return account_id, balance_record_id, end_cash_balance, currency, collateral, as_of_date, origin, regulated
