"""empty message

Revision ID: f1553f3bee19
Revises: f632c464cadd
Create Date: 2019-04-25 23:37:11.173845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1553f3bee19'
down_revision = 'f632c464cadd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    # ### end Alembic commands ###