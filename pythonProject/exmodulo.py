
print('Ola, esse modulo possui uma classe Person')


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and (new_age > 0) and (new_age < 120):
            self._age = new_age

    # age = property(get_age, set_age, doc=age)

    def get_name(self):
        return self._name

    # name = property(get_name, doc=A name property)

    def __str__(self):
        return str(self._name) + ' tem ' + str(self._age) + ' anos de idade'


def mensagem():
    print("shdfgusgfhj")
