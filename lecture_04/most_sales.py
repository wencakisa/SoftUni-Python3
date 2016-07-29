from collections import defaultdict
import csv
import logging

import iso8601

logging.basicConfig(filename='error.log', level=logging.DEBUG)


def main():
    sales_data = load_sales_data(input_filename='sales.csv')

    most_sales_date, most_sales_date_amount = get_most_sales_date(sales_data)
    most_sales_hour_date, most_sales_hour, most_sales_hour_amount = get_most_sales_hour(sales_data)

    print('Most sales on {date} ({day_of_week}): {amount:.2f}$'.format(
        date=most_sales_date, day_of_week=most_sales_date.strftime('%A'),
        amount=most_sales_date_amount
    ))

    print('Most sales between {start_hour}-{end_hour}h on {date} ({day_of_week}): {amount:.2f}$'.format(
        start_hour=most_sales_hour, end_hour=most_sales_hour + 1,
        date=most_sales_hour_date, day_of_week=most_sales_hour_date.strftime('%A'),
        amount=most_sales_hour_amount
    ))


def load_sales_data(input_filename: str) -> defaultdict(int):
    sales_data = defaultdict(int)

    with open(input_filename) as f:
        for line_index, line in enumerate(csv.reader(f), start=1):
            if len(line) != 2:
                print('Invalid line detected, so ignored. Check error.log')
                logging.warning('Invalid line: {}'.format(line_index))
            else:
                dt = iso8601.parse_date(line[0]).replace(minute=0, second=0)
                price = float(line[1])

                sales_data[dt] += price

    return sales_data


def get_most_sales_date(sales_data: dict) -> tuple:
    date_sales_sum = defaultdict(int)

    for dt, prices_sum in sales_data.items():
        date_sales_sum[dt.date()] += prices_sum

    most_date_sales_amount = max(date_sales_sum.values())

    for d, amount in date_sales_sum.items():
        if amount == most_date_sales_amount:
            return d, amount


def get_most_sales_hour(sales_data: dict) -> tuple:
    hour_sales_sum = {}
    dates = set([dt.date() for dt in sales_data.keys()])

    for d in dates:
        hour_dict = {}

        for dt, prices_sum in sales_data.items():
            if dt.date() == d:
                hour_dict[dt.hour] = prices_sum

        hour_sales_sum[d] = hour_dict

    most_hour_sales_amount = max(max(hour_dict.values()) for hour_dict in hour_sales_sum.values())

    for d, hour_dict in hour_sales_sum.items():
        for hour, amount in hour_dict.items():
            if amount == most_hour_sales_amount:
                return d, hour, amount

if __name__ == '__main__':
    main()
