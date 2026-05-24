import json
from src.product import Product
from src.category import Category


def load_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = []
    for cat_data in data['categories']:
        products = [Product(**prod) for prod in cat_data['products']]
        category = Category(cat_data['name'], cat_data['description'], products)
        categories.append(category)
    return categories
