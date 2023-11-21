import click
from pizzas import Pizza
import pizza_actions


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if pizza.lower() not in Pizza.get_subclasses_lower_names():
        print("Такой пиццы нет в меню")
    else:
        pizza_actions.bake(pizza_name=pizza)
        if delivery:
            pizza_actions.deliver(pizza_name=pizza)


@cli.command()
def menu():
    """Выводит меню"""

    # Хотелось бы видеть конкретные пиццы объектами класса Pizza,
    # но задание было несколько другое, поэтому пришлось использовать
    # не очень красивую рефлексию, которая хорошо себя покажет при
    # дальнейших расширениях кода. Например, при увеличении количества
    # потомков класса Pizza
    pizzas = Pizza.get_subclasses()
    for subclass_of_pizza in pizzas:
        print(subclass_of_pizza.dict(subclass_of_pizza))


if __name__ == "__main__":
    cli()
