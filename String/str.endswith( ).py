def ends_with(string, word):
    for i in range(len(word)):
        if ord(string[len(string) - len(word) + i]) != ord(word[i]):
            return False

    return True


string = "I am learning python"
word = "python"
print(ends_with(string, word))


string = "I am learning python"
word = "py"
print(ends_with(string, word))