"""empty message

Revision ID: 787cc58a8f70
Revises: ccdad58e9884
Create Date: 2019-09-05 11:59:38.687715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '787cc58a8f70'
down_revision = 'ccdad58e9884'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('importance', sa.String(length=10), nullable=True))
    op.add_column('tasks', sa.Column('status', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'status')
    op.drop_column('tasks', 'importance')
    # ### end Alembic commands ###
