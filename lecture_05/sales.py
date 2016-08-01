from decimal import Decimal, InvalidOperation
from datetime import timezone

import iso8601

EXPECTED_COLUMNS = 5

COLUMN_ITEM_ID = 0
COLUMN_ITEM_COUNTRY = 1
COLUMN_ITEM_CITY = 2
COLUMN_ITEM_TIMESTAMP = 3
COLUMN_ITEM_PRICE = 4


class Item:
    def __init__(self, item_id, country, city, timestamp, price):
        self.item_id = item_id
        self.country = country
        self.city = city
        self.timestamp = timestamp
        self.price = price

    def __repr__(self):
        return '{}: {}'.format(self.__class__, str(self.__dict__))


def load_sales_data(gen) -> list:
    """
    Expected columns in catalog file:
        1. Идентификационен номер на артикула;
        2. Държава, в която е била извършена продажбата (ISO code)
        3. Име на град, в която е била извършена продажбата;
        4. Дата/час на продажбата с timezone, във формат ISO8601;
        5. Цена на продажбата (цените на един и същ артикул в различните държави са различни)


    Result:
        [
            Item(
                item_id="561712",
                country="ES",
                city="Murcia",
                ts="2015-12-11T17:14:05+01:00",
                price="43.21"
            ),
            Item(
                ...
            )
            ..
        ]
    """
    return [
        Item(
            item_id=row[COLUMN_ITEM_ID],
            country=row[COLUMN_ITEM_COUNTRY],
            city=row[COLUMN_ITEM_CITY],
            timestamp=row[COLUMN_ITEM_TIMESTAMP],
            price=row[COLUMN_ITEM_PRICE]
        )
        for row in gen
        if len(row) == EXPECTED_COLUMNS
    ]


def test_sales_data(sales: list) -> bool:
    for sale_item in sales:
        try:
            sale_item.timestamp = iso8601.parse_date(sale_item.timestamp).astimezone(timezone.utc)
            sale_item.price = Decimal(sale_item.price)
        except iso8601.ParseError as pe:
            print(str(pe))
            return False
        except InvalidOperation:
            print('Unable to parse decimal {}'.format(sale_item.price))
            return False

    return True

if __name__ == '__main__':
    pass
