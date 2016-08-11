from typing import Dict
import csv

EXPECTED_COLUMNS = 8


class CatalogEntry:
    def __init__(self, item_key, category_name):
        self.item_key = str(item_key)
        self.category_name = str(category_name)

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, str(self.__dict__))


def load_catalog_data(catalog_filename: str) -> Dict[str, CatalogEntry]:
    with open(catalog_filename, mode='r', encoding='utf-8') as f:
        return {
            row[0]: CatalogEntry(item_key=row[0], category_name=row[5])
            for row in csv.reader(f)
            if len(row) == EXPECTED_COLUMNS
        }

if __name__ == '__main__':
    pass
