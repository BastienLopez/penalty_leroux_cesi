import random
from typing import List, Dict, Union

class Fruit:
    def __init__(self, id: int, name: str, quantity: int, price: float):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

class OrderItem:
    def __init__(self, fruit_id: int, quantity: int, unit_price: float):
        self.fruit_id = fruit_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.amount = quantity * unit_price

class Order:
    def __init__(self):
        self.order_items: List[OrderItem] = []
        self.amount = 0.0

#-----------------------------------------------------------------------

def generate_random_number_id() -> int:
    """Génère un id par fruit"""
    return random.randint(1, 1000)

def is_fruit(value: object) -> bool:
    """Vérifie if value = fruit"""
    return isinstance(value, Fruit)

def add_fruit_to_catalog(catalog: List[Fruit], fruit: Fruit) -> List[Fruit]:
    """Add fruit au catalogue."""
    catalog.append(fruit)
    return catalog

def remove_fruit_from_catalog(catalog: List[Fruit], fruit_id: int) -> List[Fruit]:
    """Delete un fruit du catalogue via l'id."""
    return [fruit for fruit in catalog if fruit.id != fruit_id]

def update_available_fruit_quantity(catalog: List[Fruit], fruit_id: int, quantity: int) -> List[Fruit]:
    """MAJ la quantité d'un fruit en stock"""
    for fruit in catalog:
        if fruit.id == fruit_id:
            fruit.quantity += quantity
    return catalog

def read_fruit_by_id(catalog: List[Fruit], fruit_id: int) -> Union[Fruit, None]:
    """Return un fruit par son id"""
    return next((fruit for fruit in catalog if fruit.id == fruit_id), None)

def read_fruit_by_name(catalog: List[Fruit], name: str) -> Union[Fruit, None]:
    """Return un fruit par son nom"""
    return next((fruit for fruit in catalog if fruit.name.lower() == name.lower()), None)

def sell_fruit(catalog: List[Fruit], fruit_id: int, quantity: int) -> Union[Dict[str, Union[str, float]], None]:
    """
    Vend une quantité X d'un fruit et MAJ le stock
    Return  détails de vente ou None si le fruit est introuvable ou stock insuffisant
    """
    fruit = read_fruit_by_id(catalog, fruit_id)
    if fruit is None:
        return {"error": "Fruit introuvable"}
    if fruit.quantity < quantity:
        return {"error": "Pu de Stock deso"}

    # Calcul du montant de la vente
    total_amount = quantity * fruit.price

    # MAJ du stock
    fruit.quantity -= quantity

    return {"fruit_name": fruit.name, "quantity_sold": quantity, "total_amount": total_amount}

def calculate_amount(order_items: List[OrderItem]) -> float:
    """
    Calcule le montant d'une commande à partir des OrderItems
    """
    return sum(item.amount for item in order_items)

def calculate_stock_value(catalog: List[Fruit]) -> float:
    """Calcule la valeur totale du stock"""
    return sum(fruit.price * fruit.quantity for fruit in catalog)
