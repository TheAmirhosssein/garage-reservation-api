"""create services table

Revision ID: 942cdda8d190
Revises: 5786d2dba65c
Create Date: 2025-08-31 15:58:45.564131

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "942cdda8d190"
down_revision: Union[str, Sequence[str], None] = "5786d2dba65c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""  
        CREATE TABLE services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            duration_minutes INTEGER NOT NULL
        );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE services")
