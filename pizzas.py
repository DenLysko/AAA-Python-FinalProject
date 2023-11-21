from sizes import Size, get_size_description
from typing import List


class Pizza:
    """Класс для пиццы"""

    name = None
    size = Size.NOSIZE
    ingredients = []

    def __init__(
        self,
        name: str = "Pizza",
        size: Size = Size.NOSIZE,
        ingredients: List[str] = None,
    ):
        self.name = name
        self.size = size
        self.ingredients = ingredients

    def dict(self) -> str:
        """
        Генерирует строку об ингридиента пиццы в виде словаря

        :return: строка с названием пиццы и входящими в неё ингридиентами
        """
        return "- {0}: {1}.".format(self.name, ", ".join(self.ingredients))

    def get_subclasses() -> List:
        """
        Получение всех дочерних классов класса Pizza
        """
        subclasses = []
        pizzas = Pizza.__subclasses__()
        for specific_pizza in pizzas:
            specific_pizza.__init__(specific_pizza)
            subclasses.append(specific_pizza)
        return subclasses

    def get_subclasses_lower_names() -> List[str]:
        """
        Получение названий всех пицц, являющихся подклассами класса Pizza
        """
        subclasses = Pizza.get_subclasses()
        names = []
        for specific_pizza in subclasses:
            names.append(specific_pizza.name.lower())
        return names

    def __str__(self) -> str:
        """
        Краткое описание объекта (инстанса) класса
        """
        return self.name + f". {get_size_description(self.size)}"


class Margharita(Pizza):
    """Класс для пиццы Маргарита"""

    def __init__(self, size: Size = Size.NOSIZE):
        super().__init__(
            self,
            size=size,
        )
        self.name = "Margharita"
        self.ingredients = ["tomato sauce", "mozzarella", "tomatoes"]


class Pepperoni(Pizza):
    """Класс для пиццы Пепперони"""

    def __init__(self, size: Size = Size.NOSIZE):
        super().__init__(
            self,
            size=size,
        )
        self.name = "Pepperoni"
        self.ingredients = ["tomato sauce", "mozzarella", "pepperoni"]


class Hawaiian(Pizza):
    """Класс для гавайской пиццы"""

    def __init__(self, size: Size = Size.NOSIZE):
        super().__init__(
            self,
            size=size,
        )
        self.name = "Hawaiian"
        self.ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapples"]
