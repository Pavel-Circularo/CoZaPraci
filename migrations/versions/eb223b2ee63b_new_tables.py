"""new tables

Revision ID: eb223b2ee63b
Revises: 
Create Date: 2021-04-12 20:29:56.661332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb223b2ee63b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('prejudice', sa.Text(), nullable=True),
    sa.Column('reality', sa.Text(), nullable=True),
    sa.Column('day_in_life', sa.Text(), nullable=True),
    sa.Column('salary', sa.Text(), nullable=True),
    sa.Column('education', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobs')
    # ### end Alembic commands ###
