"""empty message

Revision ID: e4de8b9bf2fc
Revises: cff56c0b13a0
Create Date: 2020-03-21 01:07:24.089988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4de8b9bf2fc'
down_revision = 'cff56c0b13a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logo', sa.LargeBinary(), nullable=True),
    sa.Column('name', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client')
    # ### end Alembic commands ###
