import json

"""
    The data about people is in another file named 'people.json'

    "Because code is code, and data is data."
           - Mike Pilgrim, 'Dive Into Python 3'
"""


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
    """
    Parses JSON file into Python list
    :param input_filename: the name of the file that contains the information about people. (Format: '*.json')
    :return: data parsed into Python list
    """

    with open(input_filename, encoding='utf-8') as f:
        return json.load(f)


def get_fitting_couples(people: list) -> list:
    """
    Checks whether two people are OK to be a couple.
    Conditions:
        -> To have at least one common interest
        -> Their age difference must not be more than 6 years
        -> They mustn't have been together before
    :param people: List, containing dictionaries, consisting of information about each person.
    :return: A list from tuples.

            Each tuple contains three other tuples:
                -> tuple from male's name and age
                -> tuple from female's name and age
                -> tuple containing the common interests between them
    """

    fitting_couples = []

    males = [person for person in people if person.get('gender') == 'male']
    females = [person for person in people if person.get('gender') == 'female']

    for male in males:
        male_name, male_age, male_interests = male.get('name'), male.get('age'), male.get('interests')

        for female in females:
            female_name, female_age, female_interests = female.get('name'), female.get('age'), female.get('interests')

            common_interests = tuple(set(male_interests).intersection(female_interests))
            age_difference = abs(male_age - female_age)
            ex_partners = male_name in female.get('ex') or female_name in male.get('ex')

            if common_interests and age_difference <= 6 and not ex_partners:
                fitting_couples.append(
                    (
                        (male_name, male_age),
                        (female_name, female_age),
                        common_interests
                    )
                )

    return fitting_couples

if __name__ == '__main__':
    main()
