from timeit import default_timer as timer
import math
import time
import itertools as it



#Задание 1
if __name__ == '__main__':
    def time_of_function(function):
        def wrap(*args):
            start_time = time.perf_counter()
            end = function(*args)
            print(time.perf_counter() - start_time)
            return end

        return wrap


    @time_of_function
    def func(first, second):
        return bin(int(first, 2) + int(second, 2))


    print(func("111", "0000"))

#Вариант 2

def time_of_function(function):
    def wrap(*args, **kwargs):
        start = timer()

        function(*args, **kwargs)

        end = timer()
        print(f'Function {function.__name__} took {end - start} for execution')

    return wrap


@time_of_function
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))


factorial(100)

#Задание 2
try:
    user_input = int(input("Enter number: "))
    print([x for x in reversed(range(user_input)) if x % 3 == 0])
except:
    print("Try again")


#либо такой вариант если имелось ввиду что пользователь вводит длину массива с уже готовым результатом(деленным на 3)

user_input = int(input())
even_numbers = it.count(0, 3)
print(list(it.islice(even_numbers, user_input)))


#Задание 3   я если честно раз 10 перечитал условие и слабо понял что нужно сделать, надеюсь я правильно понял условие=)
def skip(function):
    def wrap():
        print(f' Calling {function}')
        function()
        print(f'Function {function} finished its work')

    return wrap()


@skip
def hello():
    print('Hello, world!')


hello()

# или вариант где аргументы функции выводятся в декораторе
def skip(function_to_decorate):
    def wrapper_arguments(*args, **kwargs):
        print("Результат функции которую мы обернули в декоратор:", *args, **kwargs)
        function_to_decorate(*args, **kwargs)

    return wrapper_arguments


@skip
def print_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)

print_name('Misha', 'Filatov')


# и еще один вариант
def decorator_piupiu(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):



            result = function(*args, **kwargs)

            return result
        return wrapper
    return decorator



#Задание 4
def all_triangle_numbers(n):
    for i in range(1, n + 1):
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))

all_triangle_numbers(10)

#либо такой вариант
sum = 0

for i in range(0, 100):
    sum += i
    print(f'{i+1} - {sum}')