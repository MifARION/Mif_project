try:
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
               "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" \
               "12345678901234567890 "
    encrypt = input("Enter somethings: ")
    key = int(input("Enter a key (number from 1-25): "))

    result = ""
    if key <= 0:
        print("oh no, this is low... Try again!")
    elif key > 0:
        for letter in encrypt:
            position = alphabet.find(letter)
            position_key = position + key
            if letter in alphabet:
                result = result + alphabet[position_key]
            else:
                result = result + letter
        print(f" You result {result}")
    my_file = open('godofwar.txt', 'w')
    my_file.write(result)
    my_file.close()


except IndexError:
    print("Please enter number from 1-25! Try again")
except ValueError:
    print("Enter only letters. Try again!")
    # else:
    #     print("FOR THE HORDE!!!")














