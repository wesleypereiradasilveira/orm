

import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from typing import List
from models.model_base import ModelBase
from models.retailer import Retailer
from models.batch import Batch

# SQLAlchemy ORM Many to Many Relationship
batch_invoice = sa.Table(
    "batches_invoices",
    ModelBase.metadata,
    sa.Column("invoice_id", sa.Integer, sa.ForeignKey("invoices.id")),
    sa.Column("batch_id", sa.Integer, sa.ForeignKey("batches.id"))
)

class Invoice(ModelBase):
    __tablename__: str = "invoices"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    price: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    serial_number: str = sa.Column(sa.String(45), unique=True, nullable=False)
    description: str = sa.Column(sa.String(200), nullable=False)
    # Relationships
    retailer_id: int = sa.Column(sa.Integer, sa.ForeignKey("retailers.id"))
    retailer: Retailer = orm.relationship("Retailer", lazy="joined") # SQLAlchemy ORM Config

    # SQLAlchemy ORM Many to Many Relationship
    batches: List[Batch] = orm.relationship(
        "Batch", 
        secondary=batch_invoice, 
        backref="batch", 
        lazy="dynamic"
    )

    def __repr__(self) -> int:
        return f"<Invoice: {self.id}>"
    