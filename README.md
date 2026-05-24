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