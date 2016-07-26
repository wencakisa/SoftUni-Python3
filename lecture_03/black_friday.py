import os
from random import randint

from lecture_03.avg_price_file import load_data


def main():
    input_filename_full = 'catalog_sample.csv'
    input_data = load_data(input_filename_full)

    price_increase_rates_by_category = create_price_increase_rates_by_category(input_data)

    input_data_with_changed_prices = change_prices(input_data, price_increase_rates_by_category)

    output_filename, output_extension = os.path.splitext(input_filename_full)
    output_filename_full = output_filename + '_changed' + output_extension

    with open(output_filename_full, mode='w', encoding='utf-8') as f:
        for product_info in input_data_with_changed_prices:
            f.write(','.join(product_info) + '\n')

    print('Everything written successfully in {}'.format(output_filename_full))


def create_price_increase_rates_by_category(input_data: list) -> dict:
    """
    Extracts all product categories from the products info list
    :param input_data: information about the products
    :return: dictionary with the category name as key and random percentage to increase the price by as value
    """
    product_categories = set(product_info[-3] for product_info in input_data)

    return {
        product_category: randint(60, 90)  # Random percentage rate in the range (60, 90)
        for product_category in product_categories
    }


def change_prices(input_data: list, price_increase_rates_by_category: dict) -> list:
    """
    Changes the prices of each product in the catalog
    :param input_data: list, containing all the needed data
    :param price_increase_rates_by_category: dictionary with the category name as key and random percentage to increase
    the price by as value
    :return: new list with changed prices
    """
    result = []

    for product_info in input_data:
        category = str(product_info[-3])
        price = float(product_info[-1])

        changed_price = price + (price_increase_rates_by_category[category] / 100 * price)
        rounded_price = round(changed_price, 2)
        product_info[-1] = str(rounded_price)

        result.append(product_info)

    return result


if __name__ == '__main__':
    main()
