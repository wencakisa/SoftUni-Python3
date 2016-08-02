def main():
    try:
        input_item_id = str(input())
        sales_filename = str(input())

        sales_data = load_sales_data(sales_filename, input_item_id)

        print(min(sales_data, key=lambda n: n[1])[0])
    except Exception:
        print('INVALID INPUT')


def load_sales_data(sales_filename, input_item_id):
    import csv

    result = []

    with open(sales_filename) as f:
        for row in csv.reader(f):
            item_id = row[0]
            city = row[2]
            price = float(row[4])

            if item_id == input_item_id:
                result.append((city, price))

    return result

if __name__ == '__main__':
    main()
