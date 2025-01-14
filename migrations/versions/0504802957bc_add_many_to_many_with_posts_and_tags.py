"""add many-to-many with posts and tags

Revision ID: 0504802957bc
Revises: 05e744655119
Create Date: 2025-01-14 13:14:12.971307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0504802957bc'
down_revision = '05e744655119'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###
