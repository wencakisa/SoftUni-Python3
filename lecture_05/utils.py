import os
import csv


def parse_cmd_line_params(cmd_line_params) -> tuple:
    if len(cmd_line_params) < 3:
        raise ValueError('Usage: analyze.py <catalog.csv> <sales.csv>')

    catalog_filename, sales_filename = cmd_line_params[1:3]

    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible catalog file: {}'.format(catalog_filename))
    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible sales file: {}'.format(sales_filename))

    return catalog_filename, sales_filename


def load_csv_file(filename: str):
    with open(filename, mode='r', encoding='utf-8') as f:
        yield from csv.reader(f)


def get_title_lines(title: str) -> str:
    return '-' * len(title)
