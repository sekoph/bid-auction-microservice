"""alter table bittime

Revision ID: ec55ae96f881
Revises: 8d10dae7cedc
Create Date: 2024-10-19 13:45:36.474063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec55ae96f881'
down_revision: Union[str, None] = '8d10dae7cedc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('user_bid_time', 'closing_time', type_=sa.Time(), existing_type=sa.DateTime, nullable=False)
    op.alter_column('user_bid_time', 'start_time', type_=sa.Time(), existing_type=sa.DateTime, nullable=False)


def downgrade() -> None:
    pass
