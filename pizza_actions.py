import random

MINRAND = 1
MAXRAND = 10


def bake(pizza_name: str) -> None:
    """Готовит пиццу"""
    print(f"Приготовили пиццу {pizza_name} за {random.randint(MINRAND, MAXRAND)}с!")


def deliver(pizza_name: str) -> None:
    """Доставляет пиццу"""
    print(f"Доставили пиццу {pizza_name} за {random.randint(MINRAND, MAXRAND)}с!")
