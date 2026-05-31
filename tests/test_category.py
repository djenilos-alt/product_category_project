from src import Category, Product


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
