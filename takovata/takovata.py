from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE = 'http://python3.softuni.bg/'
COOKIES = {'msid': '74748ad5de3a43a6bc0da4f9ab8c1a42'}


def main():
    urls = get_lecture_urls()

    for index, url in enumerate(urls, start=1):
        url_full = urljoin(BASE, url)
        filename = 'lecture_{}.html'.format(index)
        content = get_info(url_full)

        with open(filename, mode='w') as f:
            f.write(str(content))


def get_lecture_urls() -> set:
    r = requests.get(url=urljoin(BASE, '/student/course/'), cookies=COOKIES)

    soup = BeautifulSoup(r.text, 'html.parser')

    return sorted(set(urljoin(BASE, a_tag['href']) for a_tag in soup.select('td a')))


def get_info(url_full: str):
    r = requests.get(url=url_full, cookies=COOKIES)

    soup = BeautifulSoup(r.text, 'html.parser')

    title = soup.find('h1', class_='title')
    content = soup.find('div', class_='content lecture-content fix-links')

    return """<html>
<head>
<meta charset="utf-8">
</head>
<body>
{}
{}
</body>
</html>
""".format(title, content)

if __name__ == '__main__':
    main()
