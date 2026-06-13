from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только продукты"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров строкой."""
        return "".join(
            f"{product}\n"
            for product in self.__products
        )

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(
            product.quantity
            for product in self.__products
        )

        return (
            f"{self.name}, "
            f"количество продуктов: "
            f"{total_quantity} шт."
        )

    def average_price(self) -> float:
        """Возвращает среднюю цену товаров категории."""

        try:
            total_price = sum(
                product.price
                for product in self.__products
            )

            return total_price / len(self.__products)

        except ZeroDivisionError:
            return 0
