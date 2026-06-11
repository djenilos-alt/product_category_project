from src import Smartphone


def test_smartphone_initialization():
    smartphone = Smartphone(
        "iPhone 15",
        "Смартфон",
        120000.0,
        10,
        95.5,
        "Pro",
        256,
        "Black",
    )

    assert smartphone.name == "iPhone 15"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"
