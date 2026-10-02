def my_index(t,element):
    for i in range(len(t)):
        if t[i]==element:
            return i

t=(3,4,4,4,5,6,6,6,7,7,7,8)
element=7
print(my_index(t,element))