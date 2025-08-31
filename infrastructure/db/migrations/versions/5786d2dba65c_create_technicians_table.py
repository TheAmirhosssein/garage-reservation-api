"""create technician table

Revision ID: 5786d2dba65c
Revises: 6ce672fea159
Create Date: 2025-08-31 15:53:31.316547

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5786d2dba65c"
down_revision: Union[str, Sequence[str], None] = "6ce672fea159"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE technicians (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            center_id INTEGER NOT NULL,
            FOREIGN KEY (center_id) REFERENCES center(id) ON DELETE CASCADE
        );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE technicians")
