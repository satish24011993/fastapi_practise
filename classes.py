

class Person:
    def __init__(self, name:str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

b = Person(name='Satish')

print(get_person_name(b))