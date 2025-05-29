"""empty message

Revision ID: aaba8874d85a
Revises:
Create Date: 2025-05-29 10:42:49.663261

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aaba8874d85a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("name", name=op.f("uq_users_name")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
