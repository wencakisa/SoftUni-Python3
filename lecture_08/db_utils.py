import sqlite3
from typing import Dict

from lecture_08.catalog import CatalogEntry


def create_tables(connection: sqlite3.Connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table if not exists catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200) NOT NULL,
            category_name varchar(200)
        );
    ''')

    cursor.execute('''
        create table if not exists sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200) NOT NULL,
            country varchar(3),
            city_name varchar(60),
            sale_timestamp TEXT,
            price NUMERIC
        );
    ''')


def import_catalog_into_db(catalog: Dict[str, CatalogEntry], connection: sqlite3.Connection):
    cursor = connection.cursor()

    for catalog_entry in catalog.values():
        cursor.execute(
            'insert into catalog (item_key, category_name) values (?, ?);',
            [catalog_entry.item_key, catalog_entry.category_name]
        )


def import_sales_into_db(sales, connection: sqlite3.Connection):
    cursor = connection.cursor()

    for sale in sales:
        cursor.execute(
            'insert into sales (item_key, country, city_name, sale_timestamp, price) values (?, ?, ?, ?, ?);',
            [sale.item_key, sale.country, sale.city_name, sale.timestamp.isoformat(), str(sale.price)]
        )


def import_data(catalog: Dict[str, CatalogEntry], sales_data_generator, connection: sqlite3.Connection):
    print('* Connection opened *\n')

    print('. . . Creating tables . . .')
    create_tables(connection)
    print('Tables created.')

    print('. . . Importing catalog . . .')
    import_catalog_into_db(catalog, connection)
    print('Catalog imported successfully!')

    print('. . . Importing sales . . .')
    import_sales_into_db(sales_data_generator, connection)
    print('Sales imported successfully!')


if __name__ == '__main__':
    pass
