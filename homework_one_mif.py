# Задание 1
username = str(input('What is your name?: '))
age = int(input('How old are you?'))

print(f"Hello {username} your age is {age}")

# Задание 2
user_one = int(input('Enter random number: '))
exponentiation = 132
division_remainder = 3
result = pow(user_one, exponentiation, division_remainder)
print(f"You enter {user_one} was raised to 132 degrees and left the remainder of the division by 3 and you get this {result}")




# Задание 3
number_one = int(input('Enter first number: '))
number_two = int(input('Enter second number: '))

addition = (number_one + number_two)
substraction = (number_one - number_two)
multiplication = (number_one * number_two)
exponentiation = (number_one ** number_two)
division = (number_one / number_two)
division_intg = (number_one // number_two)
division_remainder = (number_one % number_two)

print(f"{addition} addition your number \n {substraction} substraction your number \n "
      f"{multiplication} multiplication your number \n {exponentiation} exponentation your number \n"
      f"{division} division your number \n {division_intg} division integer your number \n"
      f"{division_remainder} division remainder your number")

# Задание 4
number_one = int(input('Enter first number: '))
number_two = int(input('Enter second number: '))
number_tree = int(input('Enter third number: '))

a = number_one
b = number_two
c = number_tree

result_formula = (2 * a - 8 * b / (a - b + c))

print(result_formula)

# Задание 5
number_piupiu = int(input('Enter number: '))
string_piupiu = str(input('Enter words: '))

print(string_piupiu * number_piupiu)

# Задание 6
number_one = 125
number_two = 437

ostatok_one = (number_one % 2, 3, 10, 22)
ostatok_two = (number_two % 2, 3, 10, 22)

print(f'{ostatok_one} и {ostatok_two} Это остатки от деления на 2,3,10 и 22 заданных нами чисел')

# Задание 7
number_one = int(input('Enter first number: '))
number_two = int(input('Enter second number: '))

print(number_one // number_two)

# Задание 8
number_one = str.split(input('Enter first word: '))
number_two = str.split(input('Enter second word: '))
number_three = str.split(input('Enter third word: '))
result = (number_one + number_two + number_three)
print(result)


#Задание 9
first = 15
second = 43

first = 43
second = 15

print(first, second)