"""add Department

Revision ID: 79aae2634390
Revises: 49da4ab435b9
Create Date: 2024-07-02 00:08:06.680675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79aae2634390'
down_revision = '49da4ab435b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###