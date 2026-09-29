def my_index(lst,element):
    for i in range(len(lst)):
        if lst[i]==element:
            return i



lst=[3,4,4,5,6,7,7,7,8,9,15]
element=7
print(my_index(lst,element))