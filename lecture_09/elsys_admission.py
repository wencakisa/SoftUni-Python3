import sys

import requests
from bs4 import BeautifulSoup


ADMISSION_PAGE_URL = 'http://www.elsys-bg.org/admission/math-exam-2016/'


def main():
    response = requests.get(ADMISSION_PAGE_URL)
    response_text = response.text

    soup = BeautifulSoup(response_text, 'html.parser')

    admission_table = soup.find('table', id='alt')
    table_rows = admission_table.find_all('tr')

    result = {}
    for row in table_rows:
        name_field = row.find('td', {'class': 's1'})

        if name_field is not None:
            name = name_field.get_text()

            mark_field = row.find('td', {'class': 's2'})
            mark = mark_field.get_text()

            result[name] = float(mark)

    max_padding = max(len(name) for name in result.keys())
    for name, mark in sorted(result.items(), key=lambda kv: kv[1], reverse=True):
        print('Име: {:<{}} Оценка: {}'.format(name, max_padding, mark))

if __name__ == '__main__':
    sys.exit(main())
