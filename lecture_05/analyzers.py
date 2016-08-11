from collections import Counter
from typing import Dict

from lecture_05.catalog import CatalogEntry
from lecture_05.sales import Sale


def get_title_lines(title: str) -> str:
    return '-' * len(title)


class BaseAnalyzer:
    def analyze_sale(self, sale: Sale) -> None:
        raise NotImplementedError()

    def print_results(self) -> None:
        raise NotImplementedError()


class TotalsAnalyzer(BaseAnalyzer):
    criteria_title = 'Обобщение'

    def __init__(self):
        super().__init__()

        self.total_count = 0
        self.total_amount = 0
        self.min_timestamp = None
        self.max_timestamp = None

    def analyze_sale(self, sale: Sale):
        self.total_count += 1
        self.total_amount += sale.price
        ts = sale.timestamp

        if self.min_timestamp is None or ts < self.min_timestamp:
            self.min_timestamp = ts
        if self.max_timestamp is None or ts > self.max_timestamp:
            self.max_timestamp = ts

    def print_results(self):
        print('''{title}
{lines}
    Общ брой продажби : {total_count}
    Обща сума продажби : {total_amount:.2f} €
    Средна цена на продажби : {average_amount:.2f} €
    Начало на период на данните : {start_timestamp}
    Край на период на данните : {end_timestamp}
    '''.format(title=self.criteria_title,
               lines=get_title_lines(title=self.criteria_title),
               total_count=self.total_count,
               total_amount=self.total_amount,
               average_amount=self.total_amount / self.total_count if self.total_count else None,
               start_timestamp=self.min_timestamp,
               end_timestamp=self.max_timestamp,
               ))


class AmountsGroupedAnalyzer(BaseAnalyzer):
    criteria_title = ''

    def __init__(self, catalog: Dict[str, CatalogEntry]):
        super().__init__()

        self.amounts_grouped = Counter()
        self.catalog = catalog

    def analyze_sale(self, sale: Sale):
        group_by_value = self.get_group_by_value(sale)

        self.amounts_grouped[group_by_value] += sale.price

    def print_results(self):
        top_amounts_grouped = self.amounts_grouped.most_common(5)

        max_padding = max(len(category_name) for category_name, _ in top_amounts_grouped)

        print('{} (top 5)\n{}'.format(self.criteria_title, get_title_lines(title=self.criteria_title)))
        for category_name, price in top_amounts_grouped:
            print('\t{:<{}} : {:.2f} €'.format(category_name, max_padding, price))
        print('')

    def get_group_by_value(self, sale: Sale) -> str:
        raise NotImplementedError()


class AmountsByCategoryAnalyzer(AmountsGroupedAnalyzer):
    criteria_title = 'Сума на продажби по категории'

    def get_group_by_value(self, sale: Sale) -> str:
        return self.catalog.get(sale.item_id, None).category_name


class AmountsByCityAnalyzer(AmountsGroupedAnalyzer):
    criteria_title = 'Сума на продажби по градове'

    def get_group_by_value(self, sale: Sale) -> str:
        return '{} ({})'.format(sale.city, sale.country)


class AmountsByHourAnalyzer(AmountsGroupedAnalyzer):
    criteria_title = 'Часове с най-голяма сума продажби'

    def get_group_by_value(self, sale: Sale) -> str:
        return sale.timestamp.replace(minute=0, second=0).strftime('%Y-%m-%d %H:%M')
