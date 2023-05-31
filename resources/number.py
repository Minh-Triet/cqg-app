from flask_restful import Resource

from model.number import add_number, NumberTestModel


class NumberTest(Resource):
    @classmethod
    def post(cls):
        m = 0
        # abcd = 0
        # acd = get_groupId()
        # if acd is None:
        #     acd = 0
        NumberTestModel.GroupID =  1
        while m < 10:
            m += 1
            NumberTestModel.data = m
            add_number()

        return 'done'

    @classmethod
    def get(cls):
        ad = ''
        NumberTestModel.query.filter(NumberTestModel.GroupID).update({NumberTestModel.data:'a'})
        # a = da.data
        # print(da.data)
        # for row in da:
        #     print("GroupID:", row)
        #     ad += row
        # print(ad)
        # result = db.session.execute(text("select GroupID from test"))
        # for row in result:
        #     print("GroupID:", row["GroupID"])
        return 'de'
