"""empty message

Revision ID: fa5875562e92
Revises: ae6e5eeb3335
Create Date: 2019-12-26 00:25:04.092689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa5875562e92'
down_revision = 'ae6e5eeb3335'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_table', sa.Column('added_string_field', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test_table', 'added_string_field')
    # ### end Alembic commands ###