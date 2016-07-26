from collections import defaultdict

from lecture_03.avg_price_file import load_data, get_average_price


def main():
    input_filename = 'catalog_sample.csv'
    input_data = load_data(input_filename)

    grouped_by_genders = group_by_genders(input_data)

    for gender, avg_price in sorted(grouped_by_genders.items(), key=lambda n: n[1], reverse=True):
        print('{}: {:.2f}$'.format(gender, avg_price))


def group_by_genders(input_data: list) -> dict:
    product_info_genders = defaultdict(list)

    for product_info in input_data:
        gender = str(product_info[-2])
        price = float(product_info[-1])

        product_info_genders[gender].append(price)

    return {
        gender: get_average_price(prices)
        for gender, prices in product_info_genders.items()
    }


if __name__ == '__main__':
    main()
