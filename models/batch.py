

import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.model_base import ModelBase
from models.popsicle_type import PopsicleType

class Batch(ModelBase):
    __tablename__: str = "batches"

    id: int = sa.Column(sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True)
    created_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    quantity: int = sa.Column(sa.Integer, nullable=False)
    # Relationships
    popsicle_type_id: int = sa.Column(sa.Integer, sa.ForeignKey("popsicle_types.id"))
    popsicle_type: orm.Mapped[PopsicleType] = orm.relationship("PopsicleType", lazy="joined") # SQLAlchemy ORM config

    def __repr__(self) -> int:
        return f"<Batches: {self.id}>"
    