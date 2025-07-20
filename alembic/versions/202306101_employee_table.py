"""
create employee table
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('department', sa.String(length=50), nullable=False),
    )

def downgrade():
    op.drop_table('employees')
