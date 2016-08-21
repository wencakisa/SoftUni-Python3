import sys


def main():
    try:
        k = float(input())
        n = float(input())
        m = float(input())

        if k <= 0 or n <= 0 or m <= 0:
            raise ValueError('Negative prices are not supported.')

        days_to_buy_bike = get_days_to_buy_bike(
            bike_price=k,
            money_saved_a_day=n,
            money_spent_each_ten_days=m
        )

        print(days_to_buy_bike if days_to_buy_bike != -1 else 'NO BIKE FOR YOU')

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def get_days_to_buy_bike(bike_price: float, money_saved_a_day: float, money_spent_each_ten_days: float) -> int:
    """
    Counts the days needed to buy a bike with given price
    :param bike_price: price of the bike
    :param money_saved_a_day: every day you save this amount of money
    :param money_spent_each_ten_days: every tenth day you spent this amount of money
    :return: if we have enough budget to buy the bike -> return the days needed to buy it.
             if we don't have enough budget to buy the bike -> return -1
    """
    money_saved = 0
    days = 0

    while True:
        days += 1
        money_saved += money_saved_a_day

        if days % 10 == 0:
            money_saved -= money_spent_each_ten_days

            if money_saved <= 0:
                break

        if money_saved >= bike_price:
            return days

    return -1
if __name__ == '__main__':
    sys.exit(main())
