
from rich import print as rprint
from conf.db_session import create_session
from models.ingredient import Ingredient
from models.nutritive_additive import NutritiveAdditive
from models.flavour import Flavour
from models.package_type import PackageType
from models.popsicle_type import PopsicleType
from models.preservative import Preservative
from models.retailer import Retailer
from models.batch import Batch
from models.invoice import Invoice
from models.popsicle import Popsicle

def insert_nutritive_additive(sqlite: bool = False) -> NutritiveAdditive:
    rprint("Registering Nutritive Additive")

    name: str = input("What is the name of the Nutritive Additive? -> ")
    chemical_formula: str = input("What is the Chemical Formula of the Additive? -> ")
    nutritive_additive: NutritiveAdditive = NutritiveAdditive(name=name, chemical_formula=chemical_formula)

    with create_session(sqlite) as session:
        session.add(nutritive_additive)
        session.commit()

    rprint("Nutritive Additive registered successfully")
    rprint(nutritive_additive.__dict__)

    return nutritive_additive

def insert_flavour(sqlite: bool = False) -> None:
    rprint("Registering Flavour")

    name: str = input("What is the name of the Flavour? -> ")
    flavour: Flavour = Flavour(name=name)

    with create_session(sqlite) as session:
        session.add(flavour)
        session.commit()

    rprint("Flavour registered successfully")
    rprint(flavour.__dict__)

def insert_package_type(sqlite: bool = False) -> None:
    rprint("Registering Package Type")

    name: str = input("What is the name of the Package Type? -> ")
    package_type: PackageType = PackageType(name=name)

    with create_session(sqlite) as session:
        session.add(package_type)
        session.commit()

    rprint("Package Type registered successfully")
    rprint(package_type.__dict__)

def insert_popsicle_type(sqlite: bool = False) -> None:
    rprint("Registering Popsicle Type")

    name: str = input("What is the name of the Popsicle Type? -> ")
    popsicle_type: PopsicleType = PopsicleType(name=name)

    with create_session(sqlite) as session:
        session.add(popsicle_type)
        session.commit()

    rprint("Popsicle Type registered successfully")
    rprint(popsicle_type.__dict__)

def insert_ingredient(sqlite: bool = False) -> Ingredient:
    rprint("Registering Ingredient")

    name: str = input("What is the name of the Ingredient? -> ")
    ingredient: Ingredient = Ingredient(name=name)

    with create_session(sqlite) as session:
        session.add(ingredient)
        session.commit()

    rprint("Ingredient registered successfully")
    rprint(ingredient.__dict__)

    return ingredient

def insert_preservative(sqlite: bool = False) -> Preservative:
    rprint("Registering Preservative")

    name: str = input("What is the name of the Preservative? -> ")
    description: str = input("What is the description of the Preservative? -> ")
    preservative: Preservative = Preservative(name=name, description=description)

    with create_session(sqlite) as session:
        session.add(preservative)
        session.commit()

    rprint("Preservative registered successfully")
    rprint(preservative.__dict__)

    return preservative

def insert_retailer(sqlite: bool = False) -> None:
    rprint("Registering Retailer")

    taxid: str = input("What is the taxid of the Retailer? -> ")
    business_name: str = input("What is the business name of the Retailer? -> ")
    contact_name: str = input("What is the contact name of the Retailer? -> ")
    retailer: Retailer = Retailer(taxid=taxid, business_name=business_name, contact_name=contact_name)

    with create_session(sqlite) as session:
        session.add(retailer)
        session.commit()

    rprint("Retailer registered successfully")
    rprint(retailer.__dict__)

def insert_batch(sqlite: bool = False) -> Batch:
    rprint("Registering Batch")

    popsicle_type_id: int = input("What is the id of the Popsicle type? -> ")
    quantity: int = input("What is the quantity of Popsicle in Batch? -> ")
    batch: Batch = Batch(popsicle_type_id=popsicle_type_id, quantity=quantity)

    with create_session(sqlite) as session:
        session.add(batch)
        session.commit()

    rprint("Batch registered successfully")
    rprint(batch.__dict__)

    return batch

def insert_invoice(sqlite: bool = False) -> None:
    rprint("Registering Invoice")

    price: float = input("What is the total price of the Invoice? -> ")
    serial_number: str = input("What is the serial number of the Invoice? -> ")
    description: str = input("What is the description of the Invoice? -> ")
    retailer_id: int = input("What is the id of the Retailer? -> ")
    invoice: Invoice = Invoice(price=price, serial_number=serial_number, description=description, retailer_id=retailer_id)

    for _ in range(2):
        batch = insert_batch(sqlite)
        invoice.batches.append(batch)

    with create_session(sqlite) as session:
        session.add(invoice)
        session.commit()

    rprint("Invoice registered successfully")
    rprint(invoice.__dict__)

def insert_popsicle(sqlite: bool = False) -> None:
    rprint("Registering Popsicle")

    price: float = input("What is the total price of the Popsicle? -> ")
    flavour_id: int = input("What is the flavour id of the Popsicle? -> ")
    popsicle_type_id: int = input("What is the popsicle type id of the Popsicle? -> ")
    package_type_id: int = input("What is the package id of the the Popsicle? -> ")
    popsicle: Popsicle = Popsicle(price=price, flavour_id=flavour_id, popsicle_type_id=popsicle_type_id, package_type_id=package_type_id)

    for _ in range(2):
        ingredient = insert_ingredient(sqlite)
        preservative = insert_preservative(sqlite)
        nutritive_additive = insert_nutritive_additive(sqlite)

        popsicle.ingredients.append(ingredient)
        popsicle.preservatives.append(preservative)
        popsicle.nutritive_additives.append(nutritive_additive)

    with create_session(sqlite) as session:
        session.add(popsicle)
        session.commit()

    rprint("Popsicle registered successfully")
    rprint(popsicle.__dict__)

if __name__ == "__main__":
    # insert_nutritive_additive(sqlite=True) # SQLite
    # insert_nutritive_additive() # Postgres

    # insert_flavour()
    # insert_package_type()
    # insert_popsicle_type()
    # insert_ingredient()
    # insert_preservative()
    # insert_retailer()
    # insert_batch()
    # insert_invoice()
    insert_popsicle()
