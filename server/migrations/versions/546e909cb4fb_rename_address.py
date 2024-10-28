"""rename address

Revision ID: 546e909cb4fb
Revises: 945ff7d7f1fa
Create Date: 2024-07-02 10:25:31.374482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '546e909cb4fb'
down_revision = '945ff7d7f1fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.alter_column('departments', 'address',  new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')

    # ### end Alembic commands ###