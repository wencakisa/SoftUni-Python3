from decimal import Decimal
from datetime import datetime, timezone
import csv

import iso8601

EXPECTED_COLUMNS = 5


class Sale:
    def __init__(self, item_id, country, city, timestamp, price):
        self.item_id = str(item_id)
        self.country = str(country)
        self.city = str(city)

        if not isinstance(timestamp, datetime):
            self.timestamp = iso8601.parse_date(str(timestamp))
        else:
            self.timestamp = timestamp

        if self.timestamp.tzinfo is None:
            raise ValueError('Naive datetimes are not supported.')
        else:
            self.timestamp = self.timestamp.astimezone(timezone.utc)

        if not isinstance(price, Decimal):
            self.price = Decimal(price)
        else:
            self.price = price

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, str(self.__dict__))


def load_sales_data(sales_filename: str):
    with open(sales_filename, mode='r', encoding='utf-8') as f:
        for row in csv.reader(f):
            if len(row) == EXPECTED_COLUMNS:
                yield Sale(
                    item_id=row[0],
                    country=row[1],
                    city=row[2],
                    timestamp=row[3],
                    price=row[4]
                )

if __name__ == '__main__':
    pass
