"""empty message

Revision ID: 6a6b71cd78e8
Revises: d5aed9ce7c8f
Create Date: 2020-03-22 17:30:29.915485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a6b71cd78e8'
down_revision = 'd5aed9ce7c8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_1', sa.String(), nullable=True),
    sa.Column('phone_2', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('address_1', sa.String(), nullable=True),
    sa.Column('address_2', sa.String(), nullable=True),
    sa.Column('facebook', sa.String(), nullable=True),
    sa.Column('whatsapp', sa.String(), nullable=True),
    sa.Column('linkdeIn', sa.String(), nullable=True),
    sa.Column('instagram', sa.String(), nullable=True),
    sa.Column('blog', sa.String(), nullable=True),
    sa.Column('areaDoCliente', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    # ### end Alembic commands ###