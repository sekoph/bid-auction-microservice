""" create bidtime table

Revision ID: 8d10dae7cedc
Revises: 757556358f65
Create Date: 2024-10-19 01:49:09.415913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, time


# revision identifiers, used by Alembic.
revision: str = '8d10dae7cedc'
down_revision: Union[str, None] = '757556358f65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_bid_time',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date_created', sa.DateTime(), default=datetime),
        sa.Column('start_time', sa.DateTime(), default=time),
        sa.Column('closing_time', sa.DateTime(), default=time),
        sa.Column('product_id', sa.Integer(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    pass
