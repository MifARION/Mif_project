# Задание 1

romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def parse_roman(roman):
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[roman[i]] < romans[roman[i + 1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]
    return result


print(parse_roman('II'))

hearthstone = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def arab_to_roman(number):
    if number <= 0:
        return ''

    priest = ''
    for arab, roman in hearthstone:
        while number >= arab:
            priest += roman
            number -= arab

    return priest


print(arab_to_roman(2))








#Задание 2
def no_numbers(file_name):
    with open(file_name, 'r') as my_file:
        data = ''.join(i for i in my_file.read() if not i.isdigit())
    with open(file_name, 'w') as my_file:
        my_file.write(data)


no_numbers()










# Задание 3,4

# Решенная задача другим методом чем в прошлый раз но с всунутым дешефратором отдельно в функцию,
# начал ее делать пока не понял что можно использовать задачу с прошлого ДЗ.
try:
    def cipher(key, text):
        if key > 26:
            key = key % 26
        caesar = ''
        for i in text:
            if ord('a') <= ord(i) <= ord('z'):
                if ord(i) + key > ord('z'):
                    caesar = caesar + chr((ord(i) + key) - 26)
                else:
                    caesar = caesar + chr(ord(i) + key)
            elif ord('A') <= ord(i) <= ord('Z'):
                if ord(i) + key > ord('Z'):
                    caesar = caesar + chr((ord(i) + key) - 26)
                else:
                    caesar = caesar + chr(ord(i) + key)
            else:
                caesar = caesar + i
        return caesar


    def dec(key, text):        #дешифратор
        if key > 26:
            key = key % 26
        caesar = ''
        for i in text:
            if ord('a') <= ord(i) <= ord('z'):
                if ord(i) - key < ord('a'):
                    caesar = caesar + chr((ord(i) - key) + 26)
                else:
                    caesar = caesar + chr(ord(i) - key)
            elif ord('A') <= ord(i) <= ord('Z'):
                if ord(i) - key < ord('A'):
                    caesar = caesar + chr((ord(i) - key) + 26)
                else:
                    caesar = caesar + chr(ord(i) - key)
            else:
                caesar = caesar + i
        return caesar


    key = input("Введите ключ - ")
    text = input("Введите текст - ")

    print(cipher(int(key), text))


except IndexError:
    print("Please enter number from 1-25! Try again")
except ValueError:
    print("Enter only letters. Try again!")
except:
    print("Try again")




# моя прошлая задача, только внутри функции, умеющая работать в обратную сторону как и дешифратор.
try:
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
               "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" \
               "12345678901234567890 "
    encrypt = input("Enter somethings: ")
    key = int(input("Enter a key (number from 1-25): "))


    def caesar(encrypt, key):
        result = ""
        if key == 0:
            print("oh no, this is low... Try again!")
        elif type(key) == int:
            for letter in encrypt:
                position = alphabet.find(letter)
                position_key = position + key
                if letter in alphabet:
                    result = result + alphabet[position_key]
                else:
                    result = result + letter
        return result


    print(caesar(encrypt, key))


except IndexError:
    print("Please enter number from 1-25! Try again")
except ValueError:
    print("Enter only letters. Try again!")








#Задание 5
try:
    def cipher(key, text):
        if key > 26:
            key = key % 26
        caesar = ''
        for i in text:
            if ord('a') <= ord(i) <= ord('z'):
                if ord(i) + key > ord('z'):
                    caesar = caesar + chr((ord(i) + key) - 26)
                else:
                    caesar = caesar + chr(ord(i) + key)
            elif ord('A') <= ord(i) <= ord('Z'):
                if ord(i) + key > ord('Z'):
                    caesar = caesar + chr((ord(i) + key) - 26)
                else:
                    caesar = caesar + chr(ord(i) + key)
            else:
                caesar = caesar + i
        return caesar


    def dec(key, text):  # дешифратор
        if key > 26:
            key = key % 26
        caesar = ''
        for i in text:
            if ord('a') <= ord(i) <= ord('z'):
                if ord(i) - key < ord('a'):
                    caesar = caesar + chr((ord(i) - key) + 26)
                else:
                    caesar = caesar + chr(ord(i) - key)
            elif ord('A') <= ord(i) <= ord('Z'):
                if ord(i) - key < ord('A'):
                    caesar = caesar + chr((ord(i) - key) + 26)
                else:
                    caesar = caesar + chr(ord(i) - key)
            else:
                caesar = caesar + i
        return caesar


    with open('godofwar.txt', 'r') as my_file:
        data = ''.join(i for i in my_file.read())
        finish = dec(3, data)
        print(finish)
        with open('ragnar.txt', 'w') as my_file_two:
            my_file_two.write(finish)

    key = input("Введите ключ - ")
    text = input("Введите текст - ")

    print(cipher(int(key), text))



except IndexError:
    print("Please enter number from 1-25! Try again")
except ValueError:
    print("Enter only letters. Try again!")
except:
    print("Try again")