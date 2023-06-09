"""empty message

Revision ID: 6dcc8bea4061
Revises: 
Create Date: 2023-05-24 16:17:54.433353

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '6dcc8bea4061'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BalanceCQG',
    sa.Column('IdentityID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('account_id', sa.NVARCHAR(), nullable=True),
    sa.Column('balance_record_id', sa.NVARCHAR(), nullable=True),
    sa.Column('currency', sa.NVARCHAR(), nullable=True),
    sa.Column('end_cash_balance', sa.NVARCHAR(), nullable=True),
    sa.Column('collateral', sa.NVARCHAR(), nullable=True),
    sa.Column('as_of_date', sa.NVARCHAR(), nullable=True),
    sa.Column('origin', sa.NVARCHAR(), nullable=True),
    sa.Column('regulated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('IdentityID')
    )
    op.create_table('Test',
    sa.Column('IdentityID', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('GroupID', sa.Integer(), nullable=True),
    sa.Column('data', sa.NVARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('IdentityID')
    )
    op.create_table('TradeCQG',
    sa.Column('IdentityID', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('MessageRaw', sa.NVARCHAR(), nullable=True),
    sa.Column('Message', sa.NVARCHAR(), nullable=True),
    sa.Column('Time', sa.DateTime(), nullable=True),
    sa.Column('OrdStatus', sa.NVARCHAR(), nullable=True),
    sa.Column('OrderID', sa.NVARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('IdentityID')
    )
    with op.batch_alter_table('jobs_stores', schema=None) as batch_op:
        batch_op.drop_index('ix_jobs_stores_next_run_time')

    op.drop_table('jobs_stores')
    op.drop_table('SchedulerManager')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SchedulerManager',
    sa.Column('Id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('ip_address', sa.NVARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('status', sa.NVARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK__Schedule__3214EC07551EAAA6')
    )
    op.create_table('jobs_stores',
    sa.Column('id', sa.NVARCHAR(length=191), autoincrement=False, nullable=False),
    sa.Column('next_run_time', sa.FLOAT(precision=53), autoincrement=False, nullable=True),
    sa.Column('job_state', mssql.VARBINARY(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='PK__jobs_sto__3213E83F42956902')
    )
    with op.batch_alter_table('jobs_stores', schema=None) as batch_op:
        batch_op.create_index('ix_jobs_stores_next_run_time', ['next_run_time'], unique=False)

    op.drop_table('TradeCQG')
    op.drop_table('Test')
    op.drop_table('BalanceCQG')
    # ### end Alembic commands ###
