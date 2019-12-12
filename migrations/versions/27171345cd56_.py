"""empty message

Revision ID: 27171345cd56
Revises: 450ae1bd03f3
Create Date: 2019-12-08 13:22:24.049662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27171345cd56'
down_revision = '450ae1bd03f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'request', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'request', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'request', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'staff', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'student', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'student', 'majors', ['major_id'], ['id'])
    op.create_foreign_key(None, 'student', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'student', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'student', ['student_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'levels', ['level_id'], ['id'])
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
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    # ### end Alembic commands ###
