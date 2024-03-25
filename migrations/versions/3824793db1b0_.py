"""empty message

Revision ID: 3824793db1b0
Revises: 
Create Date: 2024-03-25 16:05:18.228182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3824793db1b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=256), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('z_index', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('burger',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('burger_to_ingredient',
    sa.Column('burger_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['burger_id'], ['burger.id'], ),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('burger_to_ingredient')
    op.drop_table('burger')
    op.drop_table('user')
    op.drop_table('ingredient')
    # ### end Alembic commands ###