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
    with open('godofwar.txt', 'r') as my_file:
        data = ''.join(i for i in my_file.read())
        finish = caesar(data, 3)
        print(finish)
        with open('ragnar.txt', 'w') as my_file_two:
            my_file_two.write(finish)


except IndexError:
    print("Please enter number from 1-25! Try again")
except ValueError:
    print("Enter only letters. Try again!")
