from collections import Counter
from typing import List, Dict, Tuple

from sales import Item
from catalog import CatalogEntry


def get_summary(sales: List[Item]) -> Tuple:
    total_sales_count = len(sales)
    total_sales_amount = sum(sale_item.price for sale_item in sales)
    avg_sales_amount = total_sales_amount / total_sales_count if total_sales_count else None
    sale_timestamps = [sale_item.timestamp for sale_item in sales]

    return total_sales_count, total_sales_amount, avg_sales_amount, min(sale_timestamps), max(sale_timestamps)


def get_sales_by_category(catalog: Dict[str, CatalogEntry], sales: List[Item]) -> Counter:
    sales_by_category = Counter()

    for sale_item in sales:
        catalog_entry = catalog.get(sale_item.item_id, None)
        category_name = catalog_entry.category_name if catalog_entry else 'UNKNOWN'

        sales_by_category[category_name] += sale_item.price

    return sales_by_category


def get_sales_by_city(sales: List[Item]) -> Counter:
    sales_by_city = Counter()

    for sale_item in sales:
        city = '{} ({})'.format(sale_item.city, sale_item.country)

        sales_by_city[city] += sale_item.price

    return sales_by_city


def get_sales_by_timestamp(sales: List[Item]) -> Counter:
    sales_by_timestamp = Counter()

    for sale_item in sales:
        timestamp = sale_item.timestamp.replace(minute=0, second=0).strftime('%Y-%m-%d %H:%M')

        sales_by_timestamp[timestamp] += sale_item.price

    return sales_by_timestamp


def get_sales_by_gender(catalog: Dict[str, CatalogEntry], sales: List[Item]) -> Counter:
    sales_by_gender = Counter()

    for sale_item in sales:
        catalog_entry = catalog.get(sale_item.item_id, None)
        gender = catalog_entry.gender if catalog_entry else 'UNKNOWN'

        sales_by_gender[gender] += sale_item.price

    return sales_by_gender


def get_sales_by_sport(catalog: Dict[str, CatalogEntry], sales: List[Item]) -> Counter:
    sales_by_sport = Counter()

    for sale_item in sales:
        catalog_entry = catalog.get(sale_item.item_id, None)
        sport = catalog_entry.sport if catalog_entry else 'UNKNOWN'

        sales_by_sport[sport] += sale_item.price

    return sales_by_sport


def get_sales_by_criteria(catalog: Dict[str, CatalogEntry], sales: List[Item]) -> List[Tuple[str, Counter]]:
    return [
        ('Сума на продажби по категории', get_sales_by_category(catalog, sales)),
        ('Сума на продажби по градове', get_sales_by_city(sales)),
        ('Часове с най-голяма сума продажби', get_sales_by_timestamp(sales)),
        ('Сума на продажби по пол', get_sales_by_gender(catalog, sales)),
        ('Сума на продажби по спорт', get_sales_by_sport(catalog, sales))
    ]

if __name__ == '__main__':
    pass
