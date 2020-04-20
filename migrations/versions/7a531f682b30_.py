"""empty message

Revision ID: 7a531f682b30
Revises: ec89d638f240
Create Date: 2020-04-06 21:21:16.077419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a531f682b30'
down_revision = 'ec89d638f240'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('room', sa.Column('room_imga', sa.String(length=255), nullable=True))
    op.drop_column('room', 'room_img')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('room', sa.Column('room_img', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True))
    op.drop_column('room', 'room_imga')
    # ### end Alembic commands ###
