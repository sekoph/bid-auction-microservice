""" create wins table

Revision ID: 757556358f65
Revises: 542f50d93d10
Create Date: 2024-10-19 01:45:07.945451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '757556358f65'
down_revision: Union[str, None] = '542f50d93d10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_wins',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date_created', sa.DateTime(), default=datetime),
        sa.Column('bid_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_foreign_key('fk_bids_wins', 'user_wins', 'user_bids', ['bid_id'], ['id'], ondelete='CASCADE')



def downgrade() -> None:
    pass
