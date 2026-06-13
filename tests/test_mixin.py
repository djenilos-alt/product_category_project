from src import Product


def test_print_mixin(capsys):
    Product(
        "Ноутбук",
        "Игровой",
        100000.0,
        5,
    )

    captured = capsys.readouterr()

    assert "Product" in captured.out
