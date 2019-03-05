"""create users table

Revision ID: b78c1530fdf4
Revises: 
Create Date: 2019-03-05 17:25:30.066297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b78c1530fdf4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    user = op.create_table(
        'User',
        sa.Column('userId', sa.Integer, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('userName', sa.String(100), nullable=False),
        sa.Column('password', sa.String(40), nullable=False),
    )

    op.bulk_insert(
        user,
        [
            {"userName": "Admin", "password": 'admin'},
        ]
    )


def downgrade():
    op.drop_table('User')
