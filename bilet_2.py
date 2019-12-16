import calendar
import re


# Задание №1

def hight_year(year_input):
    print(calendar.isleap(year_input))


hight_year(2020)

# Задание №2


user_input = input('Enter something: ')
result = re.findall(r'\d+.?\d+|\d+', user_input)

print(result)


# Задание №3
class Key(object):
    def __init__(self, data=''):
        self.data = data

    def __eq__(self, another):
        return hasattr(another, 'data') and self.data == another.data  # __eq__Позволяет реализовать проверку на
        # равенство
        # для экземпляров пользовательских типов.

    def __hash__(self):  # __hash__ Позволяет настраивать хеширование объектов, а также управлять его возможностью.
        return hash(self.data)


a1, a2, a3 = Key('lol'), Key('lol'), Key('kek')
d = {a1: 'lol'}
