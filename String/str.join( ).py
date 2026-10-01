def my_join(lst):
    result = lst[0]
    for i in range(1, len(lst)):
        result += " " + str(lst[i])   # str() works fine now
    return result

lst = ["python", "is", "a", "programming", "language"]
print(my_join(lst))