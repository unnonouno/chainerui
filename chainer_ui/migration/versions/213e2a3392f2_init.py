"""init

Revision ID: 213e2a3392f2
Revises:
Create Date: 2017-09-05 16:23:51.900998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '213e2a3392f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('path_name',
                              sa.String(length=512), nullable=True),
                    sa.Column('name', sa.String(length=512), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('path_name')
                    )
    op.create_table('argument',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('result_id', sa.Integer(), nullable=True),
                    sa.Column('data', sa.String(length=1024), nullable=True),
                    sa.ForeignKeyConstraint(['result_id'], ['result.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('command',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('result_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(length=1024), nullable=True),
                    sa.Column('body', sa.String(length=1024), nullable=True),
                    sa.ForeignKeyConstraint(['result_id'], ['result.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('log',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('result_id', sa.Integer(), nullable=True),
                    sa.Column('data', sa.String(length=1024), nullable=True),
                    sa.ForeignKeyConstraint(['result_id'], ['result.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('snapshot',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('result_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(length=1024), nullable=True),
                    sa.Column('iteration', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['result_id'], ['result.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snapshot')
    op.drop_table('log')
    op.drop_table('command')
    op.drop_table('argument')
    op.drop_table('result')
    # ### end Alembic commands ###
