from sizes import Size
from pizzas import Pizza, Pepperoni, Hawaiian, Margharita


def test_pizza_empty_str():
    pizza = Pizza()
    assert (str(pizza)) == "Pizza. Радиус: 0 см."


def test_pizza_not_empty_str():
    pizza = Pizza(
        "4 cheese",
        Size.L,
        ["first cheese", "second cheese", "third cheese", "fourth cheese"],
    )
    assert (str(pizza)) == "4 cheese. Радиус: 16 см."


def test_pizza_dict():
    pizza = Pizza(
        "4 cheese",
        Size.L,
        ["first cheese", "second cheese", "third cheese", "fourth cheese"],
    )
    assert (len(pizza.ingredients)) == 4
    assert (
        pizza.dict()
        == "- 4 cheese: first cheese, second cheese, third cheese, fourth cheese."
    )


def test_margharita():
    assert (
        Margharita(Size.L).dict() == "- Margharita: tomato sauce, mozzarella, tomatoes."
    )
    assert str(Margharita(Size.XL)) == "Margharita. Радиус: 20 см."
    assert len(Margharita().ingredients) == 3


def test_pepperoni():
    assert (
        Pepperoni(Size.L).dict() == "- Pepperoni: tomato sauce, mozzarella, pepperoni."
    )
    assert str(Pepperoni(Size.XL)) == "Pepperoni. Радиус: 20 см."
    assert len(Pepperoni().ingredients) == 3


def test_hawaiian():
    assert (
        Hawaiian(Size.L).dict()
        == "- Hawaiian: tomato sauce, mozzarella, chicken, pineapples."
    )
    assert str(Hawaiian(Size.XL)) == "Hawaiian. Радиус: 20 см."
    assert len(Hawaiian().ingredients) == 4
