
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











