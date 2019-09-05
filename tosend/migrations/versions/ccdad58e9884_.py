"""empty message

Revision ID: ccdad58e9884
Revises: 2a4181420dee
Create Date: 2019-09-03 15:32:59.551577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccdad58e9884'
down_revision = '2a4181420dee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('is_manager', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employees', 'is_manager')
    # ### end Alembic commands ###