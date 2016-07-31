from collections import Counter


def get_title_lines(title: str) -> str:
    return '-' * len(title)


def print_summary(summary: tuple) -> None:
    title = 'Обобщение'
    total_count, total_amount, avg_amount, start_ts, end_ts = summary

    print('''{title}
{lines}
    Общ брой продажби : {total_count}
    Обща сума продажби : {total_amount:.2f} €
    Средна цена на продажби : {average_amount:.2f} €
    Начало на период на данните : {start_timestamp}
    Край на период на данните : {end_timestamp}
'''.format(title=title,
           lines=get_title_lines(title),
           total_count=total_count,
           total_amount=total_amount,
           average_amount=avg_amount,
           start_timestamp=start_ts,
           end_timestamp=end_ts,
           ))


def print_sales_by_criteria(title: str, sales_to_display: Counter, top: int=5) -> None:
    top_sales = sales_to_display.most_common(top)

    max_padding = max(len(category_name) for category_name, _ in top_sales)

    print('{} (top {})\n{}'.format(title, top, get_title_lines(title)))
    for category_name, price in top_sales:
        print('\t{:<{}} : {:.2f} €'.format(category_name, max_padding, price))

if __name__ == '__main__':
    pass
