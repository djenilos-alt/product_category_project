# Product Category Project

## Описание

Проект реализует систему категорий и товаров интернет-магазина.

Реализованы классы:

- Product
- Category

## Функциональность

- создание объектов Product;
- создание объектов Category;
- подсчет количества категорий;
- подсчет количества товаров;
- тестирование через pytest;
- проверка покрытия pytest-cov;
- проверка стиля flake8.

## Технологии

- Python 3.13
- Poetry
- Pytest
- Pytest-cov
- Flake8
- Black
- Isort
- Mypy

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/djenilos-alt/product_category_project.git

Установите зависимости:

poetry install
Запуск тестов
poetry run pytest
Проверка покрытия
poetry run pytest --cov=src --cov-report=term-missing

Репозиторий проекта

https://github.com/djenilos-alt/product_category_project
- 

## Новая функциональность

Добавлены классы-наследники:

- Smartphone
- LawnGrass

Реализованы:

- ограничения на сложение товаров разных типов;
- проверка типов при добавлении товаров в категорию;
- тестирование новой функциональности.

## Реализовано в версии 16.2

- Абстрактный класс BaseProduct.
- Класс-миксин PrintMixin.
- Product наследуется от BaseProduct и PrintMixin.
- Добавлены тесты для абстрактного класса и миксина.

## Покрытие тестами

Для проверки покрытия используется pytest-cov.

Команда запуска:

```bash
poetry run pytest --cov=src --cov-report=html

Текущее покрытие проекта: более 75%.
Отчет находится в папке htmlcov.
