from lecture_05.entries import CatalogEntry

EXPECTED_COLUMNS = 8

COLUMN_ITEM_ID = 0
COLUMN_ITEM_CATEGORY_NAME = 5


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
                category_name="SHOES"
            ),
            ...
        }
    """
    return {
        row[COLUMN_ITEM_ID]: CatalogEntry(item_id=row[COLUMN_ITEM_ID], category_name=row[COLUMN_ITEM_CATEGORY_NAME])
        for row in gen
        if len(row) == EXPECTED_COLUMNS
    }

if __name__ == '__main__':
    pass
