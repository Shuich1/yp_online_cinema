"""empty message

Revision ID: fe161d1322ff
Revises: 
Create Date: 2023-03-08 21:38:20.306142

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'fe161d1322ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='users_database'
    )
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'email'),
    sa.UniqueConstraint('id', 'email'),
    schema='users_database',
    postgresql_partition_by='RANGE (email)'
    )
    op.create_table('auth_history',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('user_agent', sa.String(length=255), nullable=True),
    sa.Column('host', sa.String(length=255), nullable=True),
    sa.Column('auth_date', sa.DateTime(), nullable=True),
    sa.Column('user_device_type', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id', 'email'], ['users_database.user.id', 'users_database.user.email'], ),
    sa.PrimaryKeyConstraint('id', 'user_device_type'),
    sa.UniqueConstraint('id', 'user_device_type'),
    schema='users_database',
    postgresql_partition_by='LIST (user_device_type)'
    )
    op.create_table('roles_users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('role_id', sa.UUID(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['users_database.role.id'], ),
    sa.ForeignKeyConstraint(['user_id', 'email'], ['users_database.user.id', 'users_database.user.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    schema='users_database'
    )
    op.execute(
            """
            CREATE TABLE IF NOT EXISTS users_database.auth_history_other
            PARTITION OF users_database.auth_history FOR VALUES IN ('other');
            CREATE TABLE IF NOT EXISTS users_database.auth_history_mobile
            PARTITION OF users_database.auth_history FOR VALUES IN ('mobile');
            CREATE TABLE IF NOT EXISTS users_database.auth_history_web
            PARTITION OF users_database.auth_history FOR VALUES IN ('web');
            CREATE TABLE IF NOT EXISTS users_database.auth_history_tablet
            PARTITION OF users_database.auth_history FOR VALUES IN (
            'tablet');
            """
    )
    op.execute(
            """
            CREATE TABLE IF NOT EXISTS users_database.user_a_f
            PARTITION OF users_database.user FOR VALUES FROM ('a') to ('f');
            CREATE TABLE IF NOT EXISTS users_database.user_g_l
            PARTITION OF users_database.user FOR VALUES FROM ('g') to ('l');
            CREATE TABLE IF NOT EXISTS users_database.user_m_r
            PARTITION OF users_database.user FOR VALUES FROM ('m') to ('r');
            CREATE TABLE IF NOT EXISTS users_database.user_s_z
            PARTITION OF users_database.user FOR VALUES FROM ('s') to ('z');
            CREATE TABLE IF NOT EXISTS users_database.user_num
            PARTITION OF users_database.user FOR VALUES FROM ('0') to ('9');
            """
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users', schema='users_database')
    op.drop_table('auth_history', schema='users_database')
    op.drop_table('user', schema='users_database')
    op.drop_table('role', schema='users_database')
    # ### end Alembic commands ###
