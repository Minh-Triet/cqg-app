from sqlalchemy import func

from ma import db


class NumberTestModel(db.Model):
    __tablename__ = 'Test'
    IdentityID = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    GroupID = db.Column(db.Integer)
    data = db.Column(db.NVARCHAR)


def add_number():
    test = NumberTestModel(
        GroupID=NumberTestModel.GroupID,
        data=NumberTestModel.data,
    )
    db.session.add(test)
    db.session.flush()
    print(test.IdentityID)
    db.session.commit()


def get_group_id():
    acd = db.session.query(func.max(NumberTestModel.GroupID)).scalar()

    return acd
