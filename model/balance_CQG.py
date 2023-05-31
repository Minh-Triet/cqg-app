import uuid

from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from ma import db


def get_uuid():
    return str(uuid.uuid4())


def save_db():
    BalanceCQG = BalanceCQGModel(
        account_id=BalanceCQGModel.account_id,
        balance_record_id=BalanceCQGModel.balance_record_id,
        currency=BalanceCQGModel.currency,
        end_cash_balance=BalanceCQGModel.end_cash_balance,
        collateral=BalanceCQGModel.collateral,
        as_of_date=BalanceCQGModel.as_of_date,
        origin=BalanceCQGModel.origin,
        regulated=BalanceCQGModel.regulated
    )
    db.session.add(BalanceCQG)
    db.session.commit()


class BalanceCQGModel(db.Model):
    __tablename__ = 'BalanceCQG'
    IdentityID = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=get_uuid())
    account_id = db.Column(db.NVARCHAR)
    balance_record_id = db.Column(db.NVARCHAR)
    currency = db.Column(db.NVARCHAR)
    end_cash_balance = db.Column(db.NVARCHAR)
    collateral = db.Column(db.NVARCHAR)
    as_of_date = db.Column(db.NVARCHAR)
    origin = db.Column(db.NVARCHAR)
    regulated = db.Column(db.Boolean)
