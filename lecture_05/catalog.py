EXPECTED_COLUMNS = 8

COLUMN_ITEM_ID = 0
COLUMN_ITEM_SPORT = 4
COLUMN_ITEM_CATEGORY_NAME = 5
COLUMN_ITEM_GENDER = 7


class CatalogEntry:
    def __init__(self, item_id, sport, category_name, gender):
        self.item_id = item_id
        self.sport = sport
        self.category_name = category_name
        self.gender = gender

    def __repr__(self):
        return '{}: {}'.format(self.__class__, str(self.__dict__))


def load_catalog_data(gen) -> dict:
    """
    Expected columns in catalog file:

        1. Идентификационен номер на артикула;
        2. Наименование на артикула;
        3. Цветове, в които артикулът е наличен;
        4. Група на артикула;
        5. Спорт, за който е предназначен артикулът;
        6. Категория
        7. Подкатегория
        8. Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета

    Result:
        {
            # item_id : CategoryEntry
            "J11328": CategoryEntry(
                item_id="J11328",
                sport="WRESTLING",
                category_name="SHOES",
                gender="Men"
            ),
            ...
        }
    """
    return {
        row[COLUMN_ITEM_ID]: CatalogEntry(
            item_id=row[COLUMN_ITEM_ID],
            sport=row[COLUMN_ITEM_SPORT],
            category_name=row[COLUMN_ITEM_CATEGORY_NAME],
            gender=row[COLUMN_ITEM_GENDER]
        )
        for row in gen
        if len(row) == EXPECTED_COLUMNS
    }

if __name__ == '__main__':
    pass
