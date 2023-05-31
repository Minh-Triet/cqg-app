import time
from datetime import datetime

import quickfix as fix
from loguru import logger


# from termcolor import colored


# def LOG_EVENT(msg):
#     print(colored(msg, "green"))
#
#
# def LOG_PACKET(packet):
#     print(colored(packet, "yellow"))


class Application(fix.Application):
    orderID = 0
    execID = 0
    isLogon = False

    def __init__(self, settings):
        super(Application, self).__init__()
        self.Settings = settings

    def genOrderID(self):
        self.orderID += 1
        return self.orderID

    def genExecID(self):
        self.execID += 1
        return str(self.execID)

    def onCreate(self, sessionID):
        self.sessionID = sessionID
        print("Session created. Session: %s" % sessionID)
        return

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print("onLogon received from server. Session: %s" % sessionID)
        self.isLogon = True
        return

    def onLogout(self, sessionID):
        print("onLogout received from server. Session: %s" % sessionID)
        return

    def toAdmin(self, message, sessionID):
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)
        if msgType.getValue() == fix.MsgType_Logon:
            message.setField(fix.SenderSubID("TestFIXSessionPersist"))
            message.setField(fix.RawData("pass"))

        print("Sending Admin message to server. Session: %s. Message: %s" % (sessionID, message))

    def toApp(self, message, sessionID):
        print("Sending Application message to server. Session: %s. Message: %s" % (sessionID, message))
        return

    def fromAdmin(self, message, sessionID):
        print("Received Admin message from server. Session: %s. Message: %s" % (sessionID, message))
        return

    def fromApp(self, message, sessionID):
        print("Received Application message to server. Session: %s. Message: %s" % (sessionID, message))
        return

    def newOrderSingle(self):
        try:
            print("New Order Single")

            orderMsg = fix.Message()

            orderMsg.getHeader().setField(self.sessionID.getBeginString())
            orderMsg.getHeader().setField(fix.MsgType(fix.MsgType_NewOrderSingle))
            orderMsg.getHeader().setField(self.sessionID.getSenderCompID())
            orderMsg.getHeader().setField(self.sessionID.getTargetCompID())
            orderMsg.getHeader().setField(fix.MsgSeqNum(self.genOrderID()))
            sendingTime = fix.SendingTime()
            sendingTime.setString(datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f"))
            orderMsg.getHeader().setField(sendingTime)

            orderMsg.setField(fix.Account("17071092"))
            orderMsg.setField(fix.ClOrdID(self.genExecID()))
            orderMsg.setField(fix.OrderQty(100))
            orderMsg.setField(fix.OrdType(fix.TriggerOrderType_LIMIT))
            orderMsg.setField(fix.Price(1.216))
            orderMsg.setField(fix.Symbol("F.US.TYAZ22"))
            orderMsg.setField(fix.Side(fix.Side_BUY))
            tranactionTime = fix.TransactTime()
            tranactionTime.setString(datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f"))
            orderMsg.setField(tranactionTime)
            orderMsg.setField(fix.OpenClose(fix.OpenClose_OPEN))

            logger.debug(orderMsg.toString())

            fix.Session.sendToTarget(orderMsg, self.sessionID)
        except Exception as e:
            print(e)

    def checkOrderStatus(self):
        try:
            print("Check Order Status")

            orderMsg = fix.Message()

            orderMsg.getHeader().setField(self.sessionID.getBeginString())
            orderMsg.getHeader().setField(fix.MsgType('UZS'))
            orderMsg.getHeader().setField(self.sessionID.getSenderCompID())
            orderMsg.getHeader().setField(self.sessionID.getTargetCompID())
            orderMsg.getHeader().setField(fix.MsgSeqNum(self.genOrderID()))
            sendingTime = fix.SendingTime()
            sendingTime.setString(datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f"))
            orderMsg.getHeader().setField(sendingTime)

            orderMsg.setField(20034, '2A28A-40E5F789D4C3B2A2')
            orderMsg.setField(263, '0')

            logger.debug(orderMsg.toString())
            logger.debug(type(orderMsg))
            logger.debug('8=FIX.4.29=9035=UZS34=149=SacombankFDC52=20230529-03:19:13.56918256=CQG_Gateway263=020034=12345510=040'.replace(
                    chr(1),'|'))
            logger.debug(' 8=FIX.4.29=10535=334=349=SacombankFDC52=20230529-03:19:13.00056=CQG_Gateway45=258=Invalid MsgType372=UZR373=1110=177'.replace(
                    chr(1),'|'))
            fix.Session.sendToTarget(orderMsg, self.sessionID)
        except Exception as e:
            logger.debug(e)

    def checkAccountData(self):
        try:
            print("Check Account Data")

            orderMsg = fix.Message()

            orderMsg.getHeader().setField(self.sessionID.getBeginString())
            orderMsg.getHeader().setField(fix.MsgType("UAR"))
            orderMsg.getHeader().setField(self.sessionID.getSenderCompID())
            orderMsg.getHeader().setField(self.sessionID.getTargetCompID())
            orderMsg.getHeader().setField(fix.MsgSeqNum(self.genOrderID()))
            sendingTime = fix.SendingTime()
            sendingTime.setString(datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f"))
            orderMsg.getHeader().setField(sendingTime)

            orderMsg.setField(fix.Account("17018382"))
            orderMsg.setField(20003, self.genExecID())

            logger.debug(orderMsg.toString())

            fix.Session.sendToTarget(orderMsg, self.sessionID)
        except Exception as e:
            print(e)


def start():
    try:
        settings = fix.SessionSettings("client.cfg")
        application = Application(settings)

        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.FileLogFactory(settings)

        initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
        initiator.start()

        bOrderSent = False
        while True:
            time.sleep(10)
            # TODO call send_order
            if bOrderSent == False and application.isLogon == True:
                # application.newOrderSingle()
                application.checkOrderStatus()
            bOrderSent = True
        # TODO print order status

        # TODO print account balance every 10 seconds
        # application.checkAccountData()

    except (fix.ConfigError, fix.RuntimeError) as e:
        print(e)


# # while True:
# #     start()
start()
