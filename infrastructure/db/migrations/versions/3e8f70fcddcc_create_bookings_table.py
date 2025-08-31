"""create bookings table

Revision ID: 3e8f70fcddcc
Revises: 942cdda8d190
Create Date: 2025-08-31 16:00:35.477646

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "3e8f70fcddcc"
down_revision: Union[str, Sequence[str], None] = "942cdda8d190"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""  
        CREATE TABLE bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            center_id INTEGER NOT NULL,
            technician_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            customer_name VARCHAR(50) NOT NULL,
            booking_type TEXT CHECK(booking_type IN ('online', 'in-person')) NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            FOREIGN KEY (center_id) REFERENCES centers(id) ON DELETE CASCADE,
            FOREIGN KEY (technician_id) REFERENCES technicians(id) ON DELETE CASCADE,
            FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
        );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE bookings")
