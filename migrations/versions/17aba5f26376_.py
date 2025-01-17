"""empty message

Revision ID: 17aba5f26376
Revises: 
Create Date: 2021-03-23 21:10:59.001948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17aba5f26376'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('pid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('property_type', sa.String(length=1000), nullable=True),
    sa.Column('location', sa.String(length=1000), nullable=True),
    sa.Column('photo', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
