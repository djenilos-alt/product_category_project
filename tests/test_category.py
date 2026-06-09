from src import Category, Product
import pytest


def test_category_str():
    products = [
        Product(
            "Ноутбук",
            "Игровой",
            100000.0,
            5,
        ),
        Product(
            "Мышь",
            "Оптическая",
            1000.0,
            10,
        ),
    ]

    category = Category(
        "Электроника",
        "Техника",
        products,
    )

    assert (
        str(category)
        == "Электроника, количество продуктов: 15 шт."
    )


def test_add_wrong_object():
    category = Category(
        "Электроника",
        "Техника",
        [],
    )

    with pytest.raises(TypeError):
        category.add_product("не товар")
