"""update rooms and event models

Revision ID: b51ed27a84de
Revises: 3974dfade8f7
Create Date: 2019-03-13 14:11:13.434263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51ed27a84de'
down_revision = '3974dfade8f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('number_of_participants', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('events', sa.Column('recurring_event_id', sa.String(), nullable=True))
    op.alter_column('events', 'event_title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('rooms', sa.Column('next_sync_token', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms', 'next_sync_token')
    op.drop_column('events', 'recurring_event_id')
    op.drop_column('events', 'number_of_participants')
    # ### end Alembic commands ###
