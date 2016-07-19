PEOPLE = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'age': 24,
        'gender': "female",
        "ex": ["Кирил", "Петър"],
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'age': 21,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'age': 34,
        'gender': "female",
        "ex": ["Борис"],
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'age': 36,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'age': 18,
        'gender': "female",
        "ex": ['Димитър'],
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'age': 27,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'age': 20,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'age': 19,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'age': 32,
        'gender': "male",
        'ex': [],
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'age': 26,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'age': 34,
        'gender': "male",
        'ex': ['Дарина'],
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'age': 22,
        'gender': "male",
        'ex': ['Галя'],
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'age': 23,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Калоян",
        'interests': ['кино', 'покер', 'пътуване', 'автомобили'],
        'age': 29,
        'gender': "male",
        'ex': [],
    },
]


def main():
    fitting_couples = get_fitting_couples(PEOPLE)

    for male_info, female_info, common_interests in fitting_couples:
        male_name, male_age = male_info
        female_name, female_age = female_info

        print('{} ({}) и {} ({}) ; общи интереси: {}'.format(
            male_name, male_age,
            female_name, female_age,
            ', '.join(common_interests)
        ))


def get_fitting_couples(people: list) -> list:
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
