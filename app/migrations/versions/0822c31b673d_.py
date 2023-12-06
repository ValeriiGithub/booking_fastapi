"""empty message

Revision ID: 0822c31b673d
Revises: 5c8f02c7e84e
Create Date: 2023-12-06 12:52:30.179050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0822c31b673d'
down_revision: Union[str, None] = '5c8f02c7e84e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
