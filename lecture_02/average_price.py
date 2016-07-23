MIN_PRICES = 4


def main():
    prices = []

    while True:
        try:
            price = float(input('Enter a price (or \'stop\'): '))
            prices.append(price)
        except ValueError:
            if len(prices) < MIN_PRICES:
                print('Enter at least {} prices...'.format(MIN_PRICES))
            else:
                break

    without_min_and_max = remove_min_and_max(prices)

    if without_min_and_max:
        print('Min price: {:.2f}'.format(min(without_min_and_max)))
        print('Max price: {:.2f}'.format(max(without_min_and_max)))
        print('Average price is: {:.2f}'.format(sum(without_min_and_max) / len(without_min_and_max)))
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
