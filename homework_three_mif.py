# Задание 1
text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore "
    "magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo "
    "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
    "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est "
    "laborum.")

sentence = text.count('. ') + text.count('! ') + text.count('? ') + 1

words = len(text.split(' '))

print(f"кол-во предложений {sentence} кол-во слов {words}")






# Задание 2
user_input = input('Enter number: ')

even = 0
odd = 0

if user_input.isdigit():
    user_input = int(user_input)
    while user_input > 0:
        if user_input % 2 == 0:
            even += 1
            print('Even')
            break
        else:
            odd += 1
        a = user_input // 10
        print('Odd')
        break
elif user_input.isalnum() or user_input.isalpha() or user_input.isspace() or user_input.islower() or user_input.isupper():
    print('This is is not a number, try again!')
else:
    print("try again")





# Задание 3
user_input = input().split(',')
string_one = ''

for i in user_input:
    string_one += str(i)
if string_one.isdigit() or string_one.isalpha() or string_one.isalnum():
    if len(string_one) < 10:
        string_one = list(string_one)
        string_one.sort(reverse=True)
        print(string_one)
    elif len(string_one) > 10:
        string_one = list(string_one)
        string_one.sort()
        print(string_one)
    elif len(string_one) == 10:
        print("list exactly 10 elements. No actions required")
    else:
        print("This is not number or text, try again")

# Задание 4
num_one = input('Enter number: ')
num_two = input('Enter number: ')

if num_one.isdigit() and num_two.isdigit():
    num_one = int(num_one)
    num_two = int(num_two)
    if num_one > num_two:
        print(num_one - num_two)
    if num_one < num_two:
        print(num_one + num_two)
    if num_one == num_two:
        print(num_one ** num_two)
elif num_one.isalnum() or num_one.isalpha() or num_one.isspace() or num_one.islower() or num_one.isupper():
    print('This is is not a number, try again!')
elif num_two.isalnum() or num_two.isalpha() or num_two.isspace() or num_two.islower() or num_two.isupper():
    print('This is is not a number, try again!')
else:
    print("try again")



# Задание 5
n_a = input('Enter number: ')
n_b = input('Enter number: ')
n_c = input('Enter number: ')
if n_a.isdigit() and n_b.isdigit() and n_c.isdigit():
    n_a = int(n_a)
    n_b = int(n_b)
    n_c = int(n_c)
    print(2 * n_a - 8 * n_b / (n_a - n_b + n_c))
elif n_a.isalnum() or n_a.isalpha() or n_a.isspace() or n_a.islower() or n_a.isupper():
    print('This is is not a number, try again!')
elif n_b.isalnum() or n_b.isalpha() or n_b.isspace() or n_b.islower() or n_b.isupper():
    print('This is is not a number, try again!')
elif n_c.isalnum() or n_c.isalpha() or n_c.isspace() or n_c.islower() or n_c.isupper():
    print('This is is not a number, try again!')
else:
    print("try again")




#Задание 6
numbers = [1, 2, 4, 4, 6, 4, 3, 8, 3, 2]
even_count = 0

for number in numbers:
    if number % 2 == 0:
        evenCount = even_count + 1

print(even_count)


#Задание 7
my_list = [5, 2, 7, 4, 0, 9, 8, 6]
racoon = True
while racoon:
    racoon = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            fox = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = fox
            racoon = True
print(my_list)

#Задание 8
fib_1 = fib_2 = 1

n_num = input("Enter row lenght: ")

if n_num.isdigit():
    n_num = int(n_num)
    if n_num < 2:
        print("Enter more than 2 numbers")
    print(fib_1, end=' ')
    print(fib_2, end=' ')
    for i in range(2, n_num):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')

    print()

elif n_num.isalnum() or n_num.isalpha() or n_num.isspace() or n_num.islower() or n_num.isupper():
    print('This is is not a number, try again!')
else:
    print("try again")



# Задание 9
user_input = input("Enter number: ")
cnt = 2

if user_input.isdigit():
    user_input = int(user_input)
    while user_input > cnt:
        if user_input % cnt == 0 and cnt != user_input:
            print('not prime')
            break
        cnt += 1
    else:
        print('prime')

elif user_input.isalnum() or user_input.isalpha() or user_input.isspace() or user_input.islower() or user_input.isupper():
    print('This is is not a number, try again!')
else:
    print("try again")
