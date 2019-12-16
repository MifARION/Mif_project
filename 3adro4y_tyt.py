import re

user_input = input('Enter something: ')
result = re.findall(r'\d+.?\d+|\d+', user_input)

print(result)

