"""add state column to devices table

Revision ID: af8e4f84b552
Revises: 1f5e47273894
Create Date: 2019-06-21 12:01:57.913494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af8e4f84b552'
down_revision = '1f5e47273894'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('state', sa.Enum('active', 'archived', 'deleted', name='statetype'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('devices', 'state')
    # ### end Alembic commands ###
