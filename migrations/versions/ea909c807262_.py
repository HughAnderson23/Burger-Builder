"""empty message

Revision ID: ea909c807262
Revises: e0d0728a35d2
Create Date: 2024-02-28 20:01:03.444926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea909c807262'
down_revision = 'e0d0728a35d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ingredient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('z_index', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ingredient', schema=None) as batch_op:
        batch_op.drop_column('z_index')

    # ### end Alembic commands ###
