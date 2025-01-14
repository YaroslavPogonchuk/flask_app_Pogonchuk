"""Creat user table

Revision ID: 29803400cc62
Revises: 96258385d3ac
Create Date: 2025-01-14 12:54:34.789750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29803400cc62'
down_revision = '96258385d3ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('author')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=100), nullable=False))

    op.drop_table('user')
    # ### end Alembic commands ###
