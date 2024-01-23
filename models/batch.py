

import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.model_base import ModelBase
from models.popsicle_type import PopsicleType

class Batch(ModelBase):
    __tablename__: str = "batches"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_date: datetime = sa.column(sa.DateTime, default=datetime.now, index=True)
    popsicle_type_id: int = sa.Column(sa.Integer, sa.ForeignKey("popsicles_type.id"))
    popsicle_type: PopsicleType = orm.relationship("PopsicleType", lazy="joined") # SQLAlchemy ORM config
    quantity: int = sa.Column(sa.Integer, nullable=False)

    def __repr__(self) -> int:
        return f"<Batches: {self.id}>"
    