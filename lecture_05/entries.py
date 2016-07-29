class Item:
    def __init__(self, item_id, country, city, timestamp, price):
        self.item_id = item_id
        self.country = country
        self.city = city
        self.timestamp = timestamp
        self.price = price

    def __repr__(self):
        return '{}: {}'.format(self.__class__, str(self.__dict__))


class CatalogEntry:
    def __init__(self, item_id, category_name):
        self.item_id = item_id
        self.category_name = category_name

    def __repr__(self):
        return '{}: {}'.format(self.__class__, str(self.__dict__))
