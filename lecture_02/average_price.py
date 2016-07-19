def main():
    prices = []

    while True:
        try:
            price = float(input('Enter a price (or \'stop\'): '))
            prices.append(price)
        except ValueError:
            if len(prices) < 4:
                print('Enter at least 4 prices...')
            else:
                break

    without_min_and_max = remove_min_and_max(prices)

    if without_min_and_max:
        print('Average price is: {}'.format(sum(without_min_and_max) / len(without_min_and_max)))
    else:
        print('List is empty.')


def remove_min_and_max(prices: list) -> list:
    min_price = min(prices)
    max_price = max(prices)

    return [
        price
        for price in prices
        if price != min_price and price != max_price
    ]

if __name__ == '__main__':
    main()
