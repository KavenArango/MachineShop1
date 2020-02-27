"""empty message

Revision ID: 11afd374ca5d
Revises: ffaff97de0fb
Create Date: 2020-02-20 10:00:32.220047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11afd374ca5d'
down_revision = 'ffaff97de0fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'booking', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'booking', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'machine_join', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'machine_shop_map', 'room', ['room_id'], ['id'])
    op.create_foreign_key(None, 'machine_shop_map', 'machine_join', ['machine_join_id'], ['id'])
    op.create_foreign_key(None, 'machines', 'machine_type', ['machine_type_id'], ['id'])
    op.create_foreign_key(None, 'post', 'users', ['author'], ['first_name'])
    op.create_foreign_key(None, 'request', 'request__des', ['requests_id'], ['id'])
    op.create_foreign_key(None, 'request', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'request', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'request', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'room', 'building', ['building_id'], ['id'])
    op.create_foreign_key(None, 'staff', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'student', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'student', 'majors', ['major_id'], ['id'])
    op.create_foreign_key(None, 'student', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'student', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'student', ['student_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student_level', type_='foreignkey')
    op.drop_constraint(None, 'student_level', type_='foreignkey')
    op.drop_constraint(None, 'student_level', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'room', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'machines', type_='foreignkey')
    op.drop_constraint(None, 'machine_shop_map', type_='foreignkey')
    op.drop_constraint(None, 'machine_shop_map', type_='foreignkey')
    op.drop_constraint(None, 'machine_join', type_='foreignkey')
    op.drop_constraint(None, 'booking', type_='foreignkey')
    op.drop_constraint(None, 'booking', type_='foreignkey')
    # ### end Alembic commands ###
