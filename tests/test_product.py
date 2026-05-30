from src import Product


def test_product_initialization():
    product = Product(
        "iPhone 15",
        "Смартфон",
        120000.0,
        10,
    )

    assert product.name == "iPhone 15"
    assert product.description == "Смартфон"
    assert product.price == 120000.0
    assert product.quantity == 10


def test_new_product():
    data = {
        "name": "Samsung",
        "description": "Телефон",
        "price": 90000.0,
        "quantity": 5,
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Samsung"
    assert product.price == 90000.0


def test_price_setter_positive():
    product = Product(
        "Ноутбук",
        "Игровой",
        100000.0,
        5,
    )

    product.price = 150000.0

    assert product.price == 150000.0


def test_price_setter_negative(capsys):
    product = Product(
        "Ноутбук",
        "Игровой",
        100000.0,
        5,
    )

    product.price = -100

    captured = capsys.readouterr()

    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100000.0
