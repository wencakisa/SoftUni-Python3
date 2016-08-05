import json
import itertools


def main():
    input_filename = 'people.json'
    people = load_people_data(input_filename)

    fitting_couples = get_fitting_couples(people)

    for male_info, female_info, common_interests in fitting_couples:
        male_name, male_age = male_info
        female_name, female_age = female_info

        print('{} ({}) и {} ({}) ; общи интереси: {}'.format(
            male_name, male_age,
            female_name, female_age,
            ', '.join(common_interests)
        ))


def load_people_data(input_filename: str) -> list:
    with open(input_filename, encoding='utf-8') as f:
        return json.load(f)


def get_fitting_couples(people: list) -> list:
    return [
        ((p1['name'], p1['age']), (p2['name'], p2['age']), set(p1['interests']) & set(p2['interests']))
        for p1, p2 in itertools.combinations(people, 2)
        if p1['gender'] != p2['gender'] and
        set(p1['interests']) & set(p2['interests']) and
        abs(p1['age'] - p2['age']) <= 6 and
        p1['name'] not in p2['ex']
    ]
if __name__ == '__main__':
    main()
