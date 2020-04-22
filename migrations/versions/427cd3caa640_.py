"""empty message

Revision ID: 427cd3caa640
Revises: be52dd481b51
Create Date: 2020-04-06 21:13:58.553061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '427cd3caa640'
down_revision = 'be52dd481b51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('FK__room__room_image__2FCF1A8A', 'room', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('FK__room__room_image__2FCF1A8A', 'room', 'room_image', ['room_image'], ['id'])
    # ### end Alembic commands ###
