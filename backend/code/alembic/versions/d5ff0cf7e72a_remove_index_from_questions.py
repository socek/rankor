"""remove index from questions

Revision ID: d5ff0cf7e72a
Revises: 27816164fc0f
Create Date: 2018-04-16 19:09:38.800548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ff0cf7e72a'
down_revision = '27816164fc0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'index')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('index', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
