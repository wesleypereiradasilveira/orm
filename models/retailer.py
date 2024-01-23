

import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

class Retailer(ModelBase):
    __tablename__: str = "retailers"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_date: datetime = sa.column(sa.DateTime, default=datetime.now, index=True)
    name: str = sa.Column(sa.String(45), unique=True, nullable=False)
    business_name: str = sa.Column(sa.String(100), nullable=True)
    contact: str = sa.Column(sa.String(100), nullable=True)

    def __repr__(self) -> str:
        return f"<Retailers: {self.name}>"
    