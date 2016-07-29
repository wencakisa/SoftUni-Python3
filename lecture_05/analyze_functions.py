from collections import defaultdict


def get_summary(sales: list) -> tuple:
    total_sales_count = len(sales)
    total_sales_amount = sum(sale_item.price for sale_item in sales)
    avg_sales_amount = total_sales_amount / total_sales_count if total_sales_count else None
    sale_timestamps = [sale_item.timestamp for sale_item in sales]

    return total_sales_count, total_sales_amount, avg_sales_amount, min(sale_timestamps), max(sale_timestamps)


def get_sales_by_category(catalog: dict, sales: list) -> defaultdict(int):
    sales_by_category = defaultdict(int)

    for sale_item in sales:
        catalog_entry = catalog.get(sale_item.item_id, None)
        category_name = catalog_entry.category_name if catalog_entry else 'UNKNOWN'

        sales_by_category[category_name] += sale_item.price

    return sales_by_category


def get_sales_by_city(sales: list) -> defaultdict(int):
    sales_by_city = defaultdict(int)

    for sale_item in sales:
        city = '{} ({})'.format(sale_item.city, sale_item.country)

        sales_by_city[city] += sale_item.price

    return sales_by_city


def get_sales_by_timestamp(sales: list) -> defaultdict(int):
    sales_by_timestamp = defaultdict(int)

    for sale_item in sales:
        timestamp = sale_item.timestamp.replace(minute=0, second=0).strftime('%Y-%m-%d %H:%M')

        sales_by_timestamp[timestamp] += sale_item.price

    return sales_by_timestamp

if __name__ == '__main__':
    pass
