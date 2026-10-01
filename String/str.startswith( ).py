def starts_with(string, word):
    for i in range(len(word)):
        if ord(string[i]) != ord(word[i]):
            return False
    return True


string = "python is a programming language"
word = "python"
print(starts_with(string, word))


string = "python is a programming language"
word = "pn"
print(starts_with(string, word))