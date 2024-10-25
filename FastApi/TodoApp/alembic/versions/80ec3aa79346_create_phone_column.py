"""Create phone column

Revision ID: 80ec3aa79346
Revises: 78de60471fc3
Create Date: 2024-10-11 13:28:42.694961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80ec3aa79346'
down_revision: Union[str, None] = '78de60471fc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    pass
