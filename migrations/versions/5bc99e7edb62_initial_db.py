"""Initial_db

Revision ID: 5bc99e7edb62
Revises: b33d3e0563c8
Create Date: 2021-11-25 19:08:32.906623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bc99e7edb62'
down_revision = 'b33d3e0563c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patente')
    # ### end Alembic commands ###
