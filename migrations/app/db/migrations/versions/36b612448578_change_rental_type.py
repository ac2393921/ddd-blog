"""change rental type

Revision ID: 36b612448578
Revises: d1ac04ef7fc5
Create Date: 2024-05-05 05:51:25.352852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '36b612448578'
down_revision: Union[str, None] = 'd1ac04ef7fc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('rental_type', sa.Enum('NEW_RELEASE', 'SEMI_NEW_RELEASE', 'OLD_RELEASE', name='rentaltype'), nullable=False, comment='レンタルタイプ'))
    op.drop_column('movies', 'value')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('value', mysql.ENUM('NEW_RELEASE', 'SEMI_NEW_RELEASE', 'OLD_RELEASE'), nullable=False, comment='レンタルタイプ'))
    op.drop_column('movies', 'rental_type')
    # ### end Alembic commands ###