"""add text to game

Revision ID: 77429ff6684d
Revises: f0696eb3e567
Create Date: 2018-05-28 19:16:24.516068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77429ff6684d'
down_revision = 'f0696eb3e567'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('welcome_message', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'welcome_message')
    # ### end Alembic commands ###
