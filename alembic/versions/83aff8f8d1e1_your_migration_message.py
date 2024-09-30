"""your_migration_message

Revision ID: 83aff8f8d1e1
Revises: 
Create Date: 2024-09-29 12:57:21.050546

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '83aff8f8d1e1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'todolist',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('category', sa.String(200), nullable=True),
    )

    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200), nullable=False),
        sa.Column('state', sa.String(200), nullable=False),
        sa.Column('todo_id', sa.Integer, sa.ForeignKey('todolist.id'), nullable=False),

    )


def downgrade() -> None:
    op.drop_table('items')
    op.drop_table('todolist')
