"""empty message

Revision ID: 34cd20b3cdb0
Revises: 696dbf33d32a
Create Date: 2020-01-26 21:45:17.117212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34cd20b3cdb0'
down_revision = '696dbf33d32a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_url', sa.String(length=48), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_url')
    # ### end Alembic commands ###
