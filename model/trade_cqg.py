from datetime import datetime

from dateutil import parser
from loguru import logger

__SOH__ = chr(1)

from ma import db
from strings.fix_message import *
from strings.fix_message_variable import *


class TradeCQG(db.Model):
    __tablename__ = 'TradeCQG'
    IdentityID = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    MessageRaw = db.Column(db.NVARCHAR)
    Message = db.Column(db.NVARCHAR)
    Time = db.Column(db.DateTime)
    OrdStatus = db.Column(db.NVARCHAR)
    OrderID = db.Column(db.NVARCHAR)


def trade_fix(message):
    Commission = ''
    CommType = ''
    ExecInst = ''
    ExecRefID = ''
    LastShares = ''
    OrigClOrdID = ''
    Text = ''
    FutSettDate = ''
    SymbolSfx = ''
    ListID = ''
    OpenClose = ''
    PossResend = ''
    StopPx = ''
    ExpireTime = ''
    DeliverToCompID = ''
    PutOrCall = ''
    StrikePrice = ''
    MaxShow = ''
    PegDifference = ''
    CouponRate = ''
    DiscretionInst = ''
    DiscretionOffset = ''
    ExpireDate = ''
    MultiLegReportingType = ''
    CFICode = ''
    Aggressive = ''
    TriggerQty = ''
    AccountName = ''
    FCMAccountNumber = ''
    CQGListID = ''
    PeggedStopPx = ''
    SalesSeriesNumber = ''
    LastModifierUsername = ''
    OrderCheckMark = ''
    ClientRegulatoryAlgorithmID = ''
    EffectiveRegulatoryAlgorithmID = ''
    OmnibusAccount = ''
    FillCareOrderRequestID = ''
    SpecificSymbol = ''
    SpecificMaturityDate = ''
    SpecificMaturityDay = ''
    SpecificMaturityMonthYear = ''
    SpecificContractDate = ''
    SpecificContractDay = ''
    SpecificContractMonthYear = ''
    IsCareOrder = ''
    SpeculationType = ''
    ExpireTimeHR = ''
    MifidAlgorithmID = ''
    MifidAlgorithmIDType = ''
    MifidAppliedAlgorithmID = ''
    MifidAppliedAlgorithmIDType = ''
    MifidInvestmentDecision = ''
    MifidInvestmentDecisionIsAlgo = ''
    ContingentSourceOrderID = ''
    NoExtraAttributes = ''
    ExtraAttributeName = ''
    ExtraAttributeValue = ''
    TradingVenueTransactionID = ''
    CommCurrency = ''
    ExternalAccountNumber = ''
    TrailPeg = ''
    BeginString = ''
    BodyLength = ''
    MsgType = ''
    MsgSeqNum = ''
    SenderCompID = ''
    SendingTime = ''
    TargetCompID = ''
    TargetSubID = ''
    DeliverToSubID = ''
    TargetLocationID = ''
    Account = ''
    AvgPx = ''
    ClOrdID = ''
    CumQty = ''
    Currency = ''
    ExecID = ''
    ExecTransType = ''
    IDSource = ''
    LastMkt = ''
    LastPx = ''
    OrderID = ''
    OrderQty = ''
    OrdStatus = ''
    OrdType = ''
    Price = ''
    SecurityID = ''
    Side = ''
    Symbol = ''
    TimeInForce = ''
    TransactTime = ''
    ExecType = ''
    LeavesQty = ''
    SecurityType = ''
    SecondaryOrderID = ''
    MaturityMonthYear = ''
    MaturityDay = ''
    SecurityExchange = ''
    MaturityDate = ''
    ManualOrderIndicator = ''
    StatementDate = ''
    OrderSource = ''
    TradeID = ''
    ChainOrderID = ''
    OrderPlacementTime = ''
    ExchangeKeyID = ''
    FillExecID = ''
    SendingTimeHR = ''
    TransactTimeHR = ''
    MifidExecutionDecision = ''
    MifidExecutionDecisionIsAlgo = ''
    TodayCutoff = ''
    ContractDate = ''
    ContractDay = ''
    ContractMonthYear = ''
    SecondaryClOrderID = ''
    ClearingBusinessDate = ''
    SecuritySubType = ''
    CustOrderHandlingInst = ''
    CheckSum = ''
    OnBehalfOfCompID = ''
    try:
        BeginString = message.getHeader().getField(8)
        BodyLength = message.getHeader().getField(9)
        MsgType = message.getHeader().getField(35)
        MsgSeqNum = message.getHeader().getField(34)
        SenderCompID = message.getHeader().getField(49)
        SendingTime = message.getHeader().getField(52)
        TargetCompID = message.getHeader().getField(56)
        TargetSubID = message.getHeader().getField(57)
        DeliverToSubID = message.getHeader().getField(129)
        TargetLocationID = message.getHeader().getField(143)
        try:
            Account = message.getField(Account_)
        except Exception:
            pass
        try:
            OrderQty = message.getField(OrderQty_)
        except Exception:
            pass
        try:
            LastMkt = message.getField(LastMkt_)
        except Exception:
            pass
        OrderID = message.getField(OrderID_)
        try:
            IDSource = message.getField(IDSource_)
        except Exception:
            pass
        try:
            ExecTransType = message.getField(ExecTransType_)
        except Exception:
            pass
        try:
            ExecID = message.getField(ExecID_)
        except Exception:
            pass
        try:
            CumQty = message.getField(CumQty_)
        except Exception:
            pass
        try:
            ClOrdID = message.getField(ClOrdID_)
        except Exception:
            pass
        try:
            AvgPx = message.getField(AvgPx_)
        except Exception:
            pass
        try:
            Currency = message.getField(Currency_)
        except Exception:
            pass
        try:
            LastPx = message.getField(LastPx_)
        except Exception:
            pass
        try:
            MaturityDate = message.getField(MaturityDate_)
        except Exception:
            pass
        try:
            SecurityExchange = message.getField(SecurityExchange_)
        except Exception:
            pass
        try:
            MaturityDay = message.getField(MaturityDay_)
        except Exception:
            pass
        try:
            MaturityMonthYear = message.getField(MaturityMonthYear_)
        except Exception:
            pass
        try:
            SecurityType = message.getField(SecurityType_)
        except Exception:
            pass
        try:
            LeavesQty = message.getField(LeavesQty_)
        except Exception:
            pass
        try:
            ExecType = message.getField(ExecType_)
        except Exception:
            pass
        try:
            TimeInForce = message.getField(TimeInForce_)
        except Exception:
            pass
        try:
            TransactTime = message.getField(TransactTime_)
        except Exception:
            pass
        try:
            Symbol = message.getField(Symbol_)
        except Exception:
            pass
        try:
            Side = message.getField(Side_)
        except Exception:
            pass
        try:
            SecurityID = message.getField(SecurityID_)
        except Exception:
            pass
        try:
            OrdType = message.getField(OrdType_)
        except Exception:
            pass
        try:
            OrdStatus = message.getField(OrdStatus_)
        except Exception:
            pass
        CheckSum = message.getTrailer().getField(10)
        try:
            FillExecID = message.getField(FillExecID_)
        except Exception:
            pass
        try:
            StatementDate = parser.parse(message.getField(StatementDate_))
        except Exception:
            pass
        try:
            TodayCutoff = parser.parse(message.getField(TodayCutoff_))
        except Exception:
            pass
        try:
            CustOrderHandlingInst = message.getField(CustOrderHandlingInst_)
        except Exception:
            pass
        try:
            SecuritySubType = message.getField(SecuritySubType_)
        except Exception:
            pass
        try:
            ContractMonthYear = message.getField(ContractMonthYear_)
        except Exception:
            pass
        try:
            ContractDay = message.getField(ContractDay_)
        except Exception:
            pass
        try:
            SecondaryClOrderID = message.getField(SecondaryClOrderID_)
        except Exception:
            pass
        try:
            ContractDate = message.getField(ContractDate_)
        except Exception:
            pass
        try:
            MifidExecutionDecisionIsAlgo = message.getField(MifidExecutionDecisionIsAlgo_)
            if MifidExecutionDecisionIsAlgo == 'Y':
                MifidExecutionDecisionIsAlgo = True
            else:
                MifidExecutionDecisionIsAlgo = False
        except Exception:
            pass
        try:
            MifidExecutionDecision = message.getField(MifidExecutionDecision_)
        except Exception:
            pass
        try:
            TransactTimeHR = message.getField(TransactTimeHR_)
        except Exception:
            pass
        try:
            SendingTimeHR = message.getField(SendingTimeHR_)
        except Exception:
            pass
        try:
            ExchangeKeyID = message.getField(ExchangeKeyID_)
        except Exception:
            pass
        try:
            OrderPlacementTime = message.getField(OrderPlacementTime_)
        except Exception:
            pass
        try:
            ChainOrderID = message.getField(ChainOrderID_)
        except Exception:
            pass
        try:
            OrderSource = message.getField(OrderSource_)
        except Exception:
            pass
        try:
            ManualOrderIndicator = message.getField(ManualOrderIndicator_)
            if ManualOrderIndicator == 'Y':
                ManualOrderIndicator = True
            else:
                ManualOrderIndicator = False
        except Exception:
            pass
        try:
            TradeID = message.getField(TradeID_)
        except Exception:
            pass
        try:
            ClearingBusinessDate = parser.parse(message.getField(ClearingBusinessDate_))
        except Exception:
            pass
        try:
            FCMAccountNumber = message.getField(FCMAccountNumber_)
        except Exception:
            pass
        try:
            AccountName = message.getField(AccountName_)
        except Exception:
            pass
        try:
            Price = message.getField(Price_)
        except Exception:
            pass
        try:
            Text = message.getField(Text_)
        except Exception:
            pass
        try:
            SecondaryOrderID = message.getField(SecondaryOrderID_)
        except Exception:
            pass
        try:
            ExecInst = message.getField(ExecInst_)
        except Exception:
            pass
        try:
            ExecRefID = message.getField(ExecRefID_)
        except Exception:
            pass
        try:
            LastShares = message.getField(LastShares_)
        except Exception:
            pass
        try:
            OrigClOrdID = message.getField(OrigClOrdID_)
        except Exception:
            pass
        try:
            FutSettDate = message.getField(FutSettDate_)
        except Exception:
            pass
        try:
            SymbolSfx = message.getField(SymbolSfx_)
        except Exception:
            pass
        try:
            ListID = message.getField(ListID_)
        except Exception:
            pass
        try:
            OpenClose = message.getField(OpenClose_)
        except Exception:
            pass
        try:
            PossResend = message.getField(PossResend_)
        except Exception:
            pass
        try:
            StopPx = message.getField(StopPx_)
        except Exception:
            pass
        try:
            ExpireTime = message.getField(ExpireTime_)
        except Exception:
            pass
        try:
            DeliverToCompID = message.getField(DeliverToCompID_)
        except Exception:
            pass
        try:
            PutOrCall = message.getField(PutOrCall_)
        except Exception:
            pass
        try:
            StrikePrice = message.getField(StrikePrice_)
        except Exception:
            pass
        try:
            MaxShow = message.getField(MaxShow_)
        except Exception:
            pass
        try:
            PegDifference = message.getField(PegDifference_)
        except Exception:
            pass
        try:
            CouponRate = message.getField(CouponRate_)
        except Exception:
            pass
        try:
            DiscretionInst = message.getField(DiscretionInst_)
        except Exception:
            pass
        try:
            DiscretionOffset = message.getField(DiscretionOffset_)
        except Exception:
            pass
        try:
            ExpireDate = message.getField(ExpireDate_)
        except Exception:
            pass
        try:
            MultiLegReportingType = message.getField(MultiLegReportingType_)
        except Exception:
            pass
        try:
            CFICode = message.getField(CFICode_)
        except Exception:
            pass
        try:
            Aggressive = message.getField(Aggressive_)
        except Exception:
            pass
        try:
            TriggerQty = message.getField(TriggerQty_)
        except Exception:
            pass
        try:
            CQGListID = message.getField(CQGListID_)
        except Exception:
            pass
        try:
            PeggedStopPx = message.getField(PeggedStopPx_)
        except Exception:
            pass
        try:
            SalesSeriesNumber = message.getField(SalesSeriesNumber_)
        except Exception:
            pass
        try:
            LastModifierUsername = message.getField(LastModifierUsername_)
        except Exception:
            pass
        try:
            OrderCheckMark = message.getField(OrderCheckMark_)
        except Exception:
            pass
        try:
            ClientRegulatoryAlgorithmID = message.getField(ClientRegulatoryAlgorithmID_)
        except Exception:
            pass
        try:
            EffectiveRegulatoryAlgorithmID = message.getField(EffectiveRegulatoryAlgorithmID_)
        except Exception:
            pass
        try:
            OmnibusAccount = message.getField(OmnibusAccount_)
        except Exception:
            pass
        try:
            FillCareOrderRequestID = message.getField(FillCareOrderRequestID_)
        except Exception:
            pass
        try:
            SpecificSymbol = message.getField(SpecificSymbol_)
        except Exception:
            pass
        try:
            SpecificMaturityDate = message.getField(SpecificMaturityDate_)
        except Exception:
            pass
        try:
            SpecificMaturityDay = message.getField(SpecificMaturityDay_)
        except Exception:
            pass
        try:
            SpecificMaturityMonthYear = message.getField(SpecificMaturityMonthYear_)
        except Exception:
            pass
        try:
            SpecificContractDate = message.getField(SpecificContractDate_)
        except Exception:
            pass
        try:
            SpecificContractDay = message.getField(SpecificContractDay_)
        except Exception:
            pass
        try:
            SpecificContractMonthYear = message.getField(SpecificContractMonthYear_)
        except Exception:
            pass
        try:
            IsCareOrder = message.getField(IsCareOrder_)
        except Exception as e:
            pass
        try:
            SpeculationType = message.getField(SpeculationType_)
        except Exception as e:
            pass
        try:
            ExpireTimeHR = message.getField(ExpireTimeHR_)
        except Exception as e:
            pass
        try:
            MifidAlgorithmID = message.getField(MifidAlgorithmID_)
        except Exception as e:
            pass
        try:
            MifidAlgorithmIDType = message.getField(MifidAlgorithmIDType_)
        except Exception as e:
            pass
        try:
            MifidAppliedAlgorithmID = message.getField(MifidAppliedAlgorithmID_)
        except Exception as e:
            pass
        try:
            MifidAppliedAlgorithmIDType = message.getField(MifidAppliedAlgorithmIDType_)
        except Exception as e:
            pass
        try:
            MifidInvestmentDecision = message.getField(MifidInvestmentDecision_)
        except Exception as e:
            pass
        try:
            MifidInvestmentDecisionIsAlgo = message.getField(MifidInvestmentDecisionIsAlgo_)
        except Exception as e:
            pass
        try:
            ContingentSourceOrderID = message.getField(ContingentSourceOrderID_)
        except Exception as e:
            pass
        try:
            NoExtraAttributes = message.getField(NoExtraAttributes_)
        except Exception as e:
            pass
        try:
            ExtraAttributeName = message.getField(ExtraAttributeName_)
        except Exception as e:
            pass
        try:
            ExtraAttributeValue = message.getField(ExtraAttributeValue_)
        except Exception as e:
            pass
        try:
            TradingVenueTransactionID = message.getField(TradingVenueTransactionID_)
        except Exception as e:
            pass
        try:
            CommCurrency = message.getField(CommCurrency_)
        except Exception as e:
            pass
        try:
            ExternalAccountNumber = message.getField(ExternalAccountNumber_)
        except Exception as e:
            pass
        try:
            TrailPeg = message.getField(TrailPeg_)
        except Exception as e:
            pass
        try:
            OnBehalfOfCompID = message.getField(OnBehalfOfCompID_)
        except Exception as e:
            pass
        try:
            Commission = message.getField(Commission_)
        except Exception as e:
            pass
        try:
            CommType = message.getField(CommType_)
        except Exception as e:
            pass

    except Exception as e:
        logger.debug(e)

    trade = TradeCQG(
        MessageRaw=message.toString().replace(__SOH__, "|"),
        Message=None,
        Time=parser.parse(str(datetime.now())),
        OrdStatus=TradeCQG.OrdStatus,
        OrderID=TradeCQG.OrderID
    )
    messageTranslate = '{' + f"\"BeginString\":\"{BeginString}\",\n\"BodyLength\":\"{BodyLength}\"," \
                             f"\n\"MsgType\":\"{getMsgType(MsgType)}\",\n\"MsgSeqNum\":\"{MsgSeqNum}\"," \
                             f"\n\"SenderCompID\":\"{SenderCompID}\",\n\"SendingTime\":\"{SendingTime}\"," \
                             f"\n\"TargetCompID\":\"{TargetCompID}\",\n\"TargetSubID\":\"{TargetSubID}\"," \
                             f"\n\"DeliverToSubID\":\"{DeliverToSubID}\",\n\"TargetLocationID\":\"{TargetLocationID}\"," \
                             f"\n\"Account\":\"{Account}\",\n\"AvgPx\":\"{AvgPx}\",\n\"ClOrdID\":\"{ClOrdID}\"," \
                             f"\n\"CumQty\":\"{CumQty}\",\n\"Currency\":\"{Currency}\",\n\"ExecID\":\"{ExecID}\"," \
                             f"\n\"ExecTransType\":\"{getExecTransType(ExecTransType)}\",\n\"IDSource\":\"{IDSource}\"," \
                             f"\n\"LastMkt\":\"{LastMkt}\",\n\"LastPx\":\"{LastPx}\",\n\"OrderID\":\"{OrderID}\"," \
                             f"\n\"OrderQty\":\"{OrderQty}\",\n\"OrdStatus\":\"{getOrdStatus(OrdStatus)}\"," \
                             f"\n\"OrdType\":\"{getOrdType(OrdType)}\",\n\"Price\":\"{Price}\",\n\"SecurityID\":\"{SecurityID}\"," \
                             f"\n\"Side\":\"{getSide(Side)}\",\n\"Symbol\":\"{Symbol}\",\n\"TimeInForce\":\"{getTimeInForce(TimeInForce)}\"," \
                             f"\n\"TransactTime\":\"{TransactTime}\",\n\"ExecType\":\"{getExecType(ExecType)}\",\n\"LeavesQty\":\"{LeavesQty}\"," \
                             f"\n\"SecurityType\":\"{getSecurityType(SecurityType)}\",\n\"SecondaryOrderID\":\"{SecondaryOrderID}\",\n\"MaturityMonthYear\":\"{MaturityMonthYear}\"," \
                             f"\n\"MaturityDay\":\"{MaturityDay}\",\n\"SecurityExchange\":\"{SecurityExchange}\",\n\"MaturityDate\":\"{MaturityDate}\"," \
                             f"\n\"ManualOrderIndicator\":\"{ManualOrderIndicator}\",\n\"StatementDate\":\"{StatementDate}\",\n\"OrderSource\":\"{OrderSource}\"," \
                             f"\n\"TradeID\":\"{TradeID}\",\n\"ChainOrderID\":\"{ChainOrderID}\",\n\"OrderPlacementTime\":\"{OrderPlacementTime}\"," \
                             f"\n\"ExchangeKeyID\":\"{ExchangeKeyID}\",\n\"FillExecID\":\"{FillExecID}\",\n\"SendingTimeHR\":\"{SendingTimeHR}\"," \
                             f"\n\"TransactTimeHR\":\"{TransactTimeHR}\",\n\"MifidExecutionDecision\":\"{MifidExecutionDecision}\"," \
                             f"\n\"MifidExecutionDecisionIsAlgo\":\"{MifidExecutionDecisionIsAlgo}\",\n\"TodayCutoff\":\"{TodayCutoff}\"," \
                             f"\n\"ContractDate\":\"{ContractDate}\",\n\"ContractDay\":\"{ContractDay}\"," \
                             f"\n\"ContractMonthYear\":\"{ContractMonthYear}\",\n\"SecondaryClOrderID\":\"{SecondaryClOrderID}\"," \
                             f"\n\"ClearingBusinessDate\":\"{ClearingBusinessDate}\",\n\"SecuritySubType\":\"{SecuritySubType}\"," \
                             f"\n\"CustOrderHandlingInst\":\"{getCustOrderHandlingInst(CustOrderHandlingInst)}\"," \
                             f"\n\"CheckSum\":\"{CheckSum}\",\n\"OnBehalfOfCompID\":\"{OnBehalfOfCompID}\"," \
                             f"\n\"Commission\":\"{Commission}\",\n\"AccountName\":\"{AccountName}\",\n\"CommType\":\"{CommType}\"," \
                             f"\n\"ExecInst\":\"{ExecInst}\",\n\"ExecRefID\":\"{ExecRefID}\",\n\"LastShares\":\"{LastShares}\"," \
                             f"\n\"OrigClOrdID\":\"{OrigClOrdID}\",\n\"Text\":\"{Text}\",\n\"FutSettDate\":\"{FutSettDate}\"," \
                             f"\n\"SymbolSfx\":\"{SymbolSfx}\",\n\"ListID\":\"{ListID}\",\n\"OpenClose\":\"{getOpenClose(OpenClose)}\"," \
                             f"\n\"PossResend\":\"{PossResend}\",\n\"StopPx\":\"{StopPx}\",\n\"ExpireTime\":\"{ExpireTime}\"," \
                             f"\n\"DeliverToCompID\":\"{DeliverToCompID}\",\n\"PutOrCall\":\"{getPutOrCall(PutOrCall)}\",\n\"StrikePrice\":\"{StrikePrice}\"," \
                             f"\n\"MaxShow\":\"{MaxShow}\",\n\"PegDifference\":\"{PegDifference}\",\n\"CouponRate\":\"{CouponRate}\"," \
                             f"\n\"DiscretionInst\":\"{getDiscretionInst(DiscretionInst)}\",\n\"DiscretionOffset\":\"{DiscretionOffset}\",\n\"ExpireDate\":\"{ExpireDate}\"," \
                             f"\n\"MultiLegReportingType\":\"{getMultiLegReportingType(MultiLegReportingType)}\",\n\"CFICode\":\"{CFICode}\",\n\"Aggressive\":\"{Aggressive}\"," \
                             f"\n\"TriggerQty\":\"{TriggerQty}\",\n\"FCMAccountNumber\":\"{FCMAccountNumber}\",\n\"CQGListID\":\"{CQGListID}\"," \
                             f"\n\"PeggedStopPx\":\"{PeggedStopPx}\",\n\"SalesSeriesNumber\":\"{SalesSeriesNumber}\",\n\"LastModifierUsername\":\"{LastModifierUsername}\"," \
                             f"\n\"OrderCheckMark\":\"{OrderCheckMark}\",\n\"ClientRegulatoryAlgorithmID\":\"{ClientRegulatoryAlgorithmID}\",\n\"EffectiveRegulatoryAlgorithmID\":\"{EffectiveRegulatoryAlgorithmID}\"," \
                             f"\n\"OmnibusAccount\":\"{OmnibusAccount}\",\n\"FillCareOrderRequestID\":\"{FillCareOrderRequestID}\",\n\"SpecificSymbol\":\"{SpecificSymbol}\"," \
                             f"\n\"SpecificMaturityDate\":\"{SpecificMaturityDate}\",\n\"SpecificMaturityDay\":\"{SpecificMaturityDay}\",\n\"SpecificMaturityMonthYear\":\"{SpecificMaturityMonthYear}\"," \
                             f"\n\"SpecificContractDate\":\"{SpecificContractDate}\",\n\"SpecificContractDay\":\"{SpecificContractDay}\",\n\"SpecificContractMonthYear\":\"{SpecificContractMonthYear}\"," \
                             f"\n\"IsCareOrder\":\"{IsCareOrder}\",\n\"SpeculationType\":\"{getSpeculationType(SpeculationType)}\",\n\"ExpireTimeHR\":\"{ExpireTimeHR}\"," \
                             f"\n\"MifidAlgorithmID\":\"{MifidAlgorithmID}\",\n\"MifidAlgorithmIDType\":\"{MifidAlgorithmIDType}\",\n\"MifidAppliedAlgorithmID\":\"{MifidAppliedAlgorithmID}\"," \
                             f"\n\"MifidAppliedAlgorithmIDType\":\"{getMifidAppliedAlgorithmIDType(MifidAppliedAlgorithmIDType)}\",\n\"MifidInvestmentDecision\":\"{MifidInvestmentDecision}\",\n\"MifidInvestmentDecisionIsAlgo\":\"{MifidInvestmentDecisionIsAlgo}\"," \
                             f"\n\"ContingentSourceOrderID\":\"{ContingentSourceOrderID}\",\n\"NoExtraAttributes\":\"{NoExtraAttributes}\",\n\"ExtraAttributeName\":\"{ExtraAttributeName}\"," \
                             f"\n\"ExtraAttributeValue\":\"{ExtraAttributeValue}\",\n\"TradingVenueTransactionID\":\"{TradingVenueTransactionID}\",\n\"CommCurrency\":\"{CommCurrency}\"," \
                             f"\n\"ExternalAccountNumber\":\"{ExternalAccountNumber}\",\n\"TrailPeg\":\"{getTrailPeg(TrailPeg)}\"" + '}'
    trade.Message = messageTranslate
    trade.OrdStatus = getOrdStatus(OrdStatus)
    trade.OrderID = OrderID
    db.session.add(trade)
    db.session.commit()
