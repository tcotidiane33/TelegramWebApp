"""add photo to diagnostics

Revision ID: 0bfc6022b536
Revises: 54b5265d2e43
Create Date: 2023-10-02 19:00:03.256724

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0bfc6022b536"
down_revision: Union[str, None] = "54b5265d2e43"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

diagnostics_photo_mapping = {
    1: "images/get-tested/mri.png",
    2: "images/get-tested/ct.png",
    3: "images/get-tested/x-ray.png",
    4: "images/get-tested/ultrasound.png",
    5: "images/get-tested/pet.png",
    6: "images/get-tested/blood-test.png",
    7: "images/get-tested/urine.png",
    8: "images/get-tested/biopsy.png",
    9: "images/get-tested/ecg.png",
    10: "images/get-tested/bone-density.png",
    11: "images/get-tested/endoscopy.png",
    12: "images/get-tested/colonoscopy.png",
}


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("diagnostics", sa.Column("photo_url", sa.String(length=256)))
    conn = op.get_bind()

    for diagnostic_id, photo_url in diagnostics_photo_mapping.items():
        conn.execute(
            sa.text(
                "UPDATE diagnostics SET photo_url = :photo_url WHERE diagnostic_id = :diagnostic_id"
            ),
            parameters=dict(
                diagnostic_id=diagnostic_id,
                photo_url=photo_url,
            ),
        )

    op.alter_column("diagnostics", "photo_url", nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("diagnostics", "photo_url")
    # ### end Alembic commands ###
