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
