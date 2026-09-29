def my_count(lst,element):
    count=0
    for i in lst:
        if i==element:
            count+=1
    return count


lst=[3,4,4,5,6,7,7,7,8,9,15]
element=7
print(my_count(lst,element))