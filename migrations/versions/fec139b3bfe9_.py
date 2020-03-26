"""empty message

Revision ID: fec139b3bfe9
Revises: 0c5f7c181286
Create Date: 2020-03-25 16:44:45.205680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fec139b3bfe9'
down_revision = '0c5f7c181286'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notification', 'date_receive',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notification', 'date_receive',
               existing_type=sa.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
