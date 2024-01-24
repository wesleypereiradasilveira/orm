

import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from typing import List, Optional
from models.model_base import ModelBase
from models.flavour import Flavour
from models.nutritive_additive import NutritiveAdditive
from models.package_type import PackageType
from models.popsicle_type import PopsicleType
from models.ingredient import Ingredient
from models.preservative import Preservative

# SQLAlchemy ORM Many to Many Relationship
ingredients_popsicle = sa.Table(
    "ingredients_popsicles",
    ModelBase.metadata,
    sa.Column("popsicle_id", sa.Integer, sa.ForeignKey("popsicles.id")),
    sa.Column("ingredient_id", sa.Integer, sa.ForeignKey("ingredients.id"))
)

preservatives_popsicle = sa.Table(
    "preservatives_popsicles",
    ModelBase.metadata,
    sa.Column("popsicle_id", sa.Integer, sa.ForeignKey("popsicles.id")),
    sa.Column("preservative_id", sa.Integer, sa.ForeignKey("preservatives.id"))
)

nutritive_additives_popsicle = sa.Table(
    "nutritive_additives_popsicles",
    ModelBase.metadata,
    sa.Column("popsicle_id", sa.Integer, sa.ForeignKey("popsicles.id")),
    sa.Column("nutritive_additive_id", sa.Integer, sa.ForeignKey("nutritive_additives.id"))
)

class Popsicle(ModelBase):
    __tablename__: str = "popsicles"

    id: int = sa.Column(sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True)
    created_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    price: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    # Relationships
    flavour_id: int = sa.Column(sa.Integer, sa.ForeignKey("flavours.id"))
    flavour: orm.Mapped[Flavour] = orm.relationship("Flavour", lazy="joined")
    package_type_id: int = sa.Column(sa.Integer, sa.ForeignKey("package_types.id"))
    package_type: orm.Mapped[PackageType] = orm.relationship("Flavour", lazy="joined")
    popsicle_type_id: int = sa.Column(sa.Integer, sa.ForeignKey("popsicle_types.id"))
    popsicle_type: orm.Mapped[PopsicleType]  = orm.relationship("PopsicleType", lazy="joined")

    # SQLAlchemy ORM One to Many or Many to Many Relationship
    ingredients: orm.Mapped[List[Ingredient]] = orm.relationship(
        "Ingredient", 
        secondary=ingredients_popsicle, 
        backref="ingredient", 
        lazy="dynamic"
    )

    preservatives: orm.Mapped[Optional[List[Preservative]]] = orm.relationship(
        "Preservative", 
        secondary=preservatives_popsicle, 
        backref="preservative", 
        lazy="dynamic"
    )

    nutritive_additives: orm.Mapped[Optional[List[NutritiveAdditive]]] = orm.relationship(
        "NutritiveAdditive", 
        secondary=nutritive_additives_popsicle, 
        backref="nutritive_additive", 
        lazy="dynamic"
    )

    def __repr__(self) -> str:
        return f"<Popsicle: {self.popsicle_type.name} with Flavour: {self.flavour.name} and Price: {self.price}>"
