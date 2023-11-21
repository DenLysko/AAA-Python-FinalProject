from sizes import (
    Size,
    get_centimetre_diameter,
    get_centimetre_radius,
    get_size_description,
)


def test_get_centimetre_diameter():
    assert get_centimetre_diameter(Size.NOSIZE) == 0
    assert get_centimetre_diameter(Size.L) == 32
    assert get_centimetre_diameter(Size.XL) == 40


def test_get_centimetre_radius():
    assert get_centimetre_radius(Size.NOSIZE) == 0
    assert get_centimetre_radius(Size.L) == 16
    assert get_centimetre_radius(Size.XL) == 20


def test_get_size_description():
    assert get_size_description(Size.NOSIZE) == "Радиус: 0 см."
    assert get_size_description(Size.L) == "Радиус: 16 см."
    assert get_size_description(Size.XL) == "Радиус: 20 см."
