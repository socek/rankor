"""add game_answer to screen

Revision ID: f0696eb3e567
Revises: 2bd26347a72a
Create Date: 2018-05-19 10:44:05.954729

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f0696eb3e567'
down_revision = '2bd26347a72a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('screen_events', sa.Column('game_answer_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(op.f('fk_screen_events_game_answer_id_game_answers'), 'screen_events', 'game_answers', ['game_answer_id'], ['id'])
    op.add_column('screens', sa.Column('game_answer_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(op.f('fk_screens_game_answer_id_game_answers'), 'screens', 'game_answers', ['game_answer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_screens_game_answer_id_game_answers'), 'screens', type_='foreignkey')
    op.drop_column('screens', 'game_answer_id')
    op.drop_constraint(op.f('fk_screen_events_game_answer_id_game_answers'), 'screen_events', type_='foreignkey')
    op.drop_column('screen_events', 'game_answer_id')
    # ### end Alembic commands ###
