"""rename owner_id to contest_id on questions

Revision ID: 008aa76af1c4
Revises: 2127774fbe45
Create Date: 2018-04-12 20:07:11.482899

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '008aa76af1c4'
down_revision = '2127774fbe45'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('questions', 'owner_id', new_column_name='contest_id')


def downgrade():
    op.alter_column('questions', 'contest_id', new_column_name='owner_id')
