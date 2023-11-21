from enum import Enum


class Size(Enum):
    """Enum для размеров пиццы"""

    NOSIZE = 0
    L = 1
    XL = 2


def get_centimetre_diameter(size: Size) -> int:
    """Получение диаметра пиццы по её размеру"""
    if isinstance(size, Size):
        TypeError
    match size:
        case Size.L:
            return 32
        case Size.XL:
            return 40
        case _:
            return 0


def get_centimetre_radius(size: Size) -> int:
    """Получение радиуса пиццы по её размеру"""
    if isinstance(size, Size):
        TypeError
    return int(get_centimetre_diameter(size) / 2)


def get_size_description(size: Size) -> str:
    """Описание радиуса пиццы в строком представлении"""
    return f"Радиус: {get_centimetre_radius(size)} см."
