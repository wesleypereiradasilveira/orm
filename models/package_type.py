

import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

class PackageType(ModelBase):
    __tablename__: str = "packages_type"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_date: datetime = sa.column(sa.DateTime, default=datetime.now, index=True)
    name: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<Package Type: {self.name}>"
