"""create service center table

Revision ID: 6ce672fea159
Revises:
Create Date: 2025-08-31 15:48:10.427663

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "6ce672fea159"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE centers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL
        );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE centers")
