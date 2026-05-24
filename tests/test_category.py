from src import Category, Product


def test_category_initialization():
    """Проверяем инициализацию объекта Category."""

    products = [
        Product("Ноутбук", "Игровой", 100000.0, 5),
        Product("Мышь", "Оптическая", 999.99, 10)
    ]

    category = Category(
        name="Электроника",
        description="Электронные устройства",
        products=products
    )

    assert category.name == "Электроника"
    assert category.description == "Электронные устройства"

    assert isinstance(category.products, list)
    assert len(category.products) == 2

    assert isinstance(category.products[0], Product)
    assert isinstance(category.products[1], Product)


def test_category_empty_products():
    """Проверяем создание категории без товаров."""

    category = Category(
        "Книги",
        "Художественная литература",
        []
    )

    assert len(category.products) == 0


def test_category_counters():
    """
    Проверяем работу атрибутов класса:
    category_count и product_count.
    """

    Category.category_count = 0
    Category.product_count = 0

    Category(
        "Книги",
        "Художественная литература",
        [
            Product(
                "Война и мир",
                "Роман",
                999.99,
                3
            )
        ]
    )

    assert Category.category_count == 1
    assert Category.product_count == 1

    Category(
        "Электроника",
        "Гаджеты",
        [
            Product(
                "Наушники",
                "Беспроводные",
                4999.99,
                5
            ),
            Product(
                "Клавиатура",
                "Механическая",
                3999.0,
                2
            )
        ]
    )

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_count_on_empty():
    """
    Проверяем увеличение category_count
    при пустом списке товаров.
    """

    Category.category_count = 0
    Category.product_count = 0

    Category(
        "Пустая категория",
        "Нет товаров",
        []
    )

    assert Category.category_count == 1
    assert Category.product_count == 0
