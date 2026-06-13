from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс продукта."""

    @property
    @abstractmethod
    def price(self):
        """Получение цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Установка цены."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        """Создание продукта из словаря."""
        pass
