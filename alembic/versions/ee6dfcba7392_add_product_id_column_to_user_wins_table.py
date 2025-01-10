"""Add product_id column to user_wins table

Revision ID: ee6dfcba7392
Revises: ec55ae96f881
Create Date: 2024-11-13 01:30:40.767739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee6dfcba7392'
down_revision: Union[str, None] = 'ec55ae96f881'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user_wins', sa.Column('product_id', sa.Integer(), nullable=False))


def downgrade() -> None:
    pass
