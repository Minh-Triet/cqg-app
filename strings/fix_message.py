def getMsgType(MsgType):
    if MsgType == '3':
        MsgType = 'Reject'
    if MsgType == '8':
        MsgType = 'Execution Report'
    if MsgType == 'F':
        MsgType = 'Order Cancel Request'
    if MsgType == '':
        MsgType = ''

    return MsgType


def getExecTransType(ExecTransType):
    if ExecTransType == '0':
        ExecTransType = 'New'
    if ExecTransType == '1':
        ExecTransType = 'Cancel'
    if ExecTransType == '2':
        ExecTransType = 'Correct'
    if ExecTransType == '3':
        ExecTransType = 'Status [response to Order Mass Status Request (UAF)]'
    if ExecTransType == '':
        ExecTransType = ''

    return ExecTransType


def getOrdStatus(OrdStatus):
    if OrdStatus == '0':
        OrdStatus = 'New'
    if OrdStatus == '1':
        OrdStatus = 'Partially filled'
    if OrdStatus == '2':
        OrdStatus = 'Filled'
    if OrdStatus == '4':
        OrdStatus = 'Canceled'
    if OrdStatus == '5':
        OrdStatus = 'Replaced'
    if OrdStatus == '6':
        OrdStatus = 'Pending Cancel'
    if OrdStatus == '8':
        OrdStatus = 'Rejected'
    if OrdStatus == '9':
        OrdStatus = 'Suspended'
    if OrdStatus == 'A':
        OrdStatus = 'Pending New'
    if OrdStatus == 'C':
        OrdStatus = 'Expired'
    if OrdStatus == 'E':
        OrdStatus = 'Pending Replace'
    if OrdStatus == '':
        OrdStatus = ''

    return OrdStatus


def getSide(Side):
    if Side == '1':
        Side = 'Buy'
    if Side == '2':
        Side = 'Sell'
    if Side == '3':
        Side = 'Buy minus'
    if Side == '4':
        Side = 'Sell plus'
    if Side == '5':
        Side = 'Sell short'
    if Side == '6':
        Side = 'Sell short exempt'
    if Side == '7':
        Side = 'Undisclosed'
    if Side == '8':
        Side = 'Cross'
    if Side == '9':
        Side = 'Cross short'
    if Side == '':
        Side = ''

    return Side


def getTimeInForce(TimeInForce):
    if TimeInForce == '0':
        TimeInForce = 'DAY'
    if TimeInForce == '1':
        TimeInForce = 'Good Till Cancel (GTC)'
    if TimeInForce == '3':
        TimeInForce = 'Immediate or Cancel (IOC)'
    if TimeInForce == '4':
        TimeInForce = 'Fill or Kill (FOK)'
    if TimeInForce == '6':
        TimeInForce = 'Good Till Date (GTD)'
    if TimeInForce == '5':
        TimeInForce = 'Good Till Crossing (GTX)'
    if TimeInForce == '':
        TimeInForce = ''

    return TimeInForce


def getExecType(ExecType):
    if ExecType == '0':
        ExecType = 'New'
    if ExecType == '1':
        ExecType = 'Partially filled'
    if ExecType == '2':
        ExecType = 'Filled'
    if ExecType == '4':
        ExecType = 'Canceled'
    if ExecType == '5':
        ExecType = 'Replaced'
    if ExecType == '6':
        ExecType = 'Pending Cancel'
    if ExecType == '8':
        ExecType = 'Rejected'
    if ExecType == '9':
        ExecType = 'Suspended'
    if ExecType == 'A':
        ExecType = 'Pending New'
    if ExecType == 'C':
        ExecType = 'Expired'
    if ExecType == 'E':
        ExecType = 'Pending Replace'
    if ExecType == '':
        ExecType = ''

    return ExecType


def getCustOrderHandlingInst(CustOrderHandlingInst):
    if CustOrderHandlingInst == 'W':
        CustOrderHandlingInst = 'Desk'
    if CustOrderHandlingInst == 'Y':
        CustOrderHandlingInst = 'Electronic'
    if CustOrderHandlingInst == 'C':
        CustOrderHandlingInst = 'Vendor-provided Platform billed by Executing Broker'
    if CustOrderHandlingInst == 'G':
        CustOrderHandlingInst = 'Sponsored Access via Exchange API or FIX provided by Executing Broker'
    if CustOrderHandlingInst == 'H':
        CustOrderHandlingInst = 'Premium Algorithmic Trading Provider billed by Executing Broker'
    if CustOrderHandlingInst == 'D':
        CustOrderHandlingInst = 'Other, including Other-provided Screen'
    if CustOrderHandlingInst == '':
        CustOrderHandlingInst = ''

    return CustOrderHandlingInst


def getOpenClose(OpenClose):
    if OpenClose == 'O':
        OpenClose = 'Open'
    if OpenClose == 'C':
        OpenClose = 'Close'
    if OpenClose == 'P':
        OpenClose = 'Close previous day'
    if OpenClose == '':
        OpenClose = ''
    return OpenClose


def getPutOrCall(PutOrCall):
    if PutOrCall == '0':
        PutOrCall = 'Put'
    if PutOrCall == '1':
        PutOrCall = 'Call'
    if PutOrCall == '':
        PutOrCall = ''
    return PutOrCall


def getDiscretionInst(DiscretionInst):
    if DiscretionInst == '0':
        DiscretionInst = 'Related to displayed price'
    if DiscretionInst == '':
        DiscretionInst = ''
    return DiscretionInst


def getMultiLegReportingType(MultiLegReportingType):
    if MultiLegReportingType == '1':
        MultiLegReportingType = 'Single security (default if not specified)'
    if MultiLegReportingType == '2':
        MultiLegReportingType = 'Individual leg of a multi-leg security'
    if MultiLegReportingType == '3':
        MultiLegReportingType = 'Multi-leg security'
    if MultiLegReportingType == '':
        MultiLegReportingType = ''
    return MultiLegReportingType


def getSpeculationType(SpeculationType):
    if SpeculationType == 'S':
        SpeculationType = 'Speculation'
    if SpeculationType == 'H':
        SpeculationType = 'Hedge'
    if SpeculationType == 'A':
        SpeculationType = 'Arbitrage'
    if SpeculationType == '':
        SpeculationType = ''
    return SpeculationType


def getMifidAppliedAlgorithmIDType(MifidAppliedAlgorithmIDType):
    if MifidAppliedAlgorithmIDType == '1':
        MifidAppliedAlgorithmIDType = 'External Mifid Algorithm ID'
    if MifidAppliedAlgorithmIDType == '2':
        MifidAppliedAlgorithmIDType = 'CQG Mifid Algorithm ID'
    if MifidAppliedAlgorithmIDType == '':
        MifidAppliedAlgorithmIDType = ''
    return MifidAppliedAlgorithmIDType


def getTrailPeg(TrailPeg):
    if TrailPeg == '1':
        TrailPeg = 'Best Bid'
    if TrailPeg == '2':
        TrailPeg = 'Best Ask'
    if TrailPeg == '3':
        TrailPeg = 'Last Trade'
    if TrailPeg == '':
        TrailPeg = ''
    return TrailPeg


def getOrdType(OrdType):
    if OrdType == '1':
        OrdType = 'Market'
    if OrdType == '2':
        OrdType = 'Limit'
    if OrdType == '3':
        OrdType = 'Stop'
    if OrdType == '4':
        OrdType = 'Stop Limit'
    if OrdType == 'I':
        OrdType = 'Funari'
    if OrdType == '':
        OrdType = ''
    return OrdType


def getSecurityType(SecurityType):
    if SecurityType == 'FUT':
        SecurityType = 'futures'
    if SecurityType == 'OPT':
        SecurityType = 'options'
    if SecurityType == 'SPD':
        SecurityType = 'spreads'
    if SecurityType == 'FOR':
        SecurityType = 'cash spot'
    if SecurityType == 'FI':
        SecurityType = 'fixed income'
    if SecurityType == '':
        SecurityType = ''
    return SecurityType
