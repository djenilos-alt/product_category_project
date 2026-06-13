from src import Product
import pytest

from src import LawnGrass, Smartphone
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


def test_add_same_type_products():
    phone_1 = Smartphone(
        "iPhone",
        "Телефон",
        100000.0,
        2,
        90.0,
        "15",
        256,
        "Black",
    )

    phone_2 = Smartphone(
        "Samsung",
        "Телефон",
        80000.0,
        1,
        85.0,
        "S24",
        256,
        "White",
    )

    assert phone_1 + phone_2 == 280000.0


def test_add_different_type_products():
    phone = Smartphone(
        "iPhone",
        "Телефон",
        100000.0,
        2,
        90.0,
        "15",
        256,
        "Black",
    )

    grass = LawnGrass(
        "Газон",
        "Трава",
        500.0,
        20,
        "Россия",
        "14 дней",
        "Зеленый",
    )

    with pytest.raises(TypeError):
        phone + grass

    def test_zero_quantity_product():
        with pytest.raises(
                ValueError,
                match="Товар с нулевым количеством не может быть добавлен",
        ):
            Product(
                "Ноутбук",
                "Игровой",
                100000.0,
                0,
            )