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


def load_sales_data(input_filename: str) -> dict:
    sales_data = {}

    with open(input_filename) as f:
        for line_index, line in enumerate(csv.reader(f), start=1):
            if len(line) != 2:
                print('Invalid line detected, so ignored. Check error.log')
                logging.warning('Invalid line: {}'.format(line_index))
            else:
                datetime = iso8601.parse_date(line[0])
                price = float(line[1])

                sales_data[datetime] = price

    return sales_data


def get_most_sales_date(sales_data: dict) -> tuple:
    sales_data_sum = defaultdict(list)

    for datetime, price in sales_data.items():
        sales_data_sum[datetime.date()].append(price)

    sales_data_sum = {date: sum(prices) for date, prices in sales_data_sum.items()}

    max_price = max(sales_data_sum.values())

    for date, price in sales_data_sum.items():
        if price == max_price:
            return date, price


def get_most_sales_hour(sales_data: dict) -> tuple:
    hour_sales_sum = defaultdict(dict)

    dates = set([datetime.date() for datetime in sales_data.keys()])

    for date in dates:
        hour_dict = defaultdict(list)

        for datetime, price in sales_data.items():
            if datetime.date() == date:
                hour_dict[datetime.hour].append(price)

        hour_sales_sum[date] = {hour: sum(prices) for hour, prices in hour_dict.items()}

    most_sales_hour_amount = max(max(hour_dict.values()) for hour_dict in hour_sales_sum.values())

    for date, hour_dict in hour_sales_sum.items():
        for hour, amount in hour_dict.items():
            if amount == most_sales_hour_amount:
                return date, hour, amount

if __name__ == '__main__':
    main()
