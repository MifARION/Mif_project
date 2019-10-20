#Задание 1

number = float(input('Enter float number: '))
round_one = round(number, 0)
round_two = round(number, 2)
round_three = round(number, 5)
print(f'{round_one} округление до 0, {round_two} округление до 2 цифр после запятой, {round_three} округление до 5 цифр после запятой')




#Задание 2
list_one = [2, 4, 7, 9, 8, 5, 3]

result = list_one.pop()
print(result)





#Задание 3
print(eval(input()))



#Задание 4
my_list = [2, 4, 7, 9, 8, 5, 3]
number_one = int(input())
number_two = int(input())

print(my_list[number_one:number_two])


#Задание 5
my_list = input()
print(list(set(my_list)))

#Задание 6
my_set_one = {1, 2, 5, 4, 7, 7, 21}
my_set_two = {4, 4, 8, 5, 1, 1, 3}

my_set_one.intersection(my_set_two)
diff_set = my_set_one.difference(my_set_two)
print(diff_set)


#Задание 7
my_list_one = [1, 2, 5, 4, 7, 7, 21]
my_list_two = [4, 4, 8, 5, 1, 1, 3]
result = my_list_one + my_list_two
print(list(set(result)))




#Задание 8
my_list = [1, 2, 5, 4, 7, 7, 21]
my_tuple = (4, 4, 8, 5, 1, 1, 3)

my_list_two = list(my_tuple)

my_list = set(my_list)
my_list_two = set(my_list_two)

result = my_list.intersection(my_list_two)

print(result)


