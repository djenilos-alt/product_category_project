from src import Category, Product


def test_add_product():
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        "Электроника",
        "Техника",
        [],
    )

    product = Product(
        "Ноутбук",
        "Игровой",
        100000.0,
        5,
    )

    category.add_product(product)

    assert Category.product_count == 1


def test_products_property():
    product = Product(
        "Ноутбук",
        "Игровой",
        100000.0,
        5,
    )

    category = Category(
        "Электроника",
        "Техника",
        [product],
    )

    expected = (
        "Ноутбук, 100000.0 руб. "
        "Остаток: 5 шт.\n"
    )

    assert category.products == expected
