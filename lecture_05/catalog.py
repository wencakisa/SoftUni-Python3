EXPECTED_COLUMNS = 8

COLUMN_ITEM_ID = 0
COLUMN_ITEM_CATEGORY_NAME = 5


class CatalogEntry:
    def __init__(self, item_id, category_name):
        self.item_id = item_id
        self.category_name = category_name

    def __repr__(self):
        return '{}: {}'.format(self.__class__, str(self.__dict__))


def load_catalog_data(gen) -> dict:
    return {
        row[COLUMN_ITEM_ID]: CatalogEntry(item_id=row[COLUMN_ITEM_ID], category_name=row[COLUMN_ITEM_CATEGORY_NAME])
        for row in gen
        if len(row) == EXPECTED_COLUMNS
    }

if __name__ == '__main__':
    pass
