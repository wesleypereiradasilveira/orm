

import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

class Retailer(ModelBase):
    __tablename__: str = "retailers"

    id: int = sa.Column(sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True)
    created_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    taxid: str = sa.Column(sa.String(45), unique=True, nullable=False)
    business_name: str = sa.Column(sa.String(100), nullable=True)
    contact_name: str = sa.Column(sa.String(100), nullable=True)

    def __repr__(self) -> str:
        return f"<Retailers: {self.name}>"
    