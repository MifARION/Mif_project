import re
import calendar
from itertools import accumulate
from operator import mul
import fileinput

#Задание 1
if __name__ == '__main__':
    with open('ragnar.txt', 'r') as my_file:
        data = ''.join(i for i in my_file.read())
        result = re.findall(r'\d\d\-\d\d\-\d{4}', data)
        print(result)


#Задание 2
try:
    user_input = int(input("Enter your year(number): "))
    print(calendar.isleap(user_input))
except:
    print("Enter year(number), try again")


#Задание 3
with open('ragnar.txt', 'r') as my_file:
    data = ''.join(i for i in my_file.read())
    result = re.findall(r'\d+\.\d*|\d+|\-\d+', data)

    result_array = []
    for elem in result:
        result_array.append(float(elem))
    result = result_array
    finish = sum(result)

    print(finish)

#Задание 4
length = 10
ratio = 2
progression = list(accumulate([ratio]*length, mul))
print(progression)



#Задание 5
for line in fileinput.input("ragnar.txt", inplace=True):
    print(re.sub('\-\d+\.\d*|\-\d+', "", line))



#Задание 6

with open('ragnar.txt', 'r') as my_file:
    data = my_file.read()
    result = re.findall(r'([A-Z]\w+(?=[\s\-][A-Z])(?:[\s\-][A-Z]\w+)+)', data)
    print(result)






