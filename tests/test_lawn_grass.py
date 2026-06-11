from src import LawnGrass


def test_lawn_grass_initialization():
    grass = LawnGrass(
        "Газон",
        "Трава",
        500.0,
        20,
        "Россия",
        "14 дней",
        "Зеленый",
    )

    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зеленый"
