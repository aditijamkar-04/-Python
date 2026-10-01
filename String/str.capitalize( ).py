def my_capitalize(string):
    result = ""

    for i in range(len(string)):
        if i == 0:
            if ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z'):
                result += chr(ord(string[i]) - 32)
            else:
                result += string[i]
        else:
            result += string[i]

    return result


string = "python is a programming language"
print(repr(my_capitalize(string)))