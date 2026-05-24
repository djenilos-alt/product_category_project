from src import Product


def test_product_initialization():
    """Проверяем корректную инициализацию Product."""

    product = Product(
        "iPhone 15",
        "Смартфон Apple",
        120000.0,
        10
    )

    assert product.name == "iPhone 15"
    assert product.description == "Смартфон Apple"
    assert product.price == 120000.0
    assert product.quantity == 10
