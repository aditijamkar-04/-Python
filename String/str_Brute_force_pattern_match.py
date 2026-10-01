string = "abababababababbbbbbababb"
pattern = "ababb"

def pattern_match(string, pattern):
    for i in range(len(string) - len(pattern) + 1):
        match = True

        for j in range(len(pattern)):
            if string[i + j] != pattern[j]:
                match = False
                break

        if match:
            return True, i

    return False, -1


print(pattern_match(string, pattern))