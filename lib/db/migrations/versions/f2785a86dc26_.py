"""empty message

Revision ID: f2785a86dc26
Revises: 5df3c743173e
Create Date: 2023-08-08 11:19:24.190086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2785a86dc26'
down_revision: Union[str, None] = '5df3c743173e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
