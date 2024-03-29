"""added online column to guestusers

Revision ID: 27da915c34d1
Revises: 34cd20b3cdb0
Create Date: 2020-01-27 09:47:14.034982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27da915c34d1'
down_revision = '34cd20b3cdb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('online', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_users_online'), 'users', ['online'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_online'), table_name='users')
    op.drop_column('users', 'online')
    # ### end Alembic commands ###
