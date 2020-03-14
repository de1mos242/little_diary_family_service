"""change date of birth to date only without time

Revision ID: d8e0aed930c7
Revises: b5eb10ef4bc9
Create Date: 2020-03-14 20:10:10.551201+00:00

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd8e0aed930c7'
down_revision = 'b5eb10ef4bc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(table_name='baby', column_name='date_of_birth', nullable=True, type_=sa.Date)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(table_name='baby', column_name='date_of_birth', nullable=True, type_=sa.DateTime)
    # ### end Alembic commands ###
