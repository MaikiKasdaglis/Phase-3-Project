"""updated columns

Revision ID: d947edd21295
Revises: ba452e8913c4
Create Date: 2023-08-07 15:51:57.291553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd947edd21295'
down_revision: Union[str, None] = 'ba452e8913c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goers', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('movies', sa.Column('title', sa.String(), nullable=True))
    op.add_column('movies', sa.Column('starring', sa.String(), nullable=True))
    op.add_column('movies', sa.Column('rating', sa.Integer(), nullable=True))
    op.drop_column('movies', 'name')
    op.add_column('theaters', sa.Column('city', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('theaters', 'city')
    op.add_column('movies', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_column('movies', 'rating')
    op.drop_column('movies', 'starring')
    op.drop_column('movies', 'title')
    op.drop_column('goers', 'age')
    # ### end Alembic commands ###
