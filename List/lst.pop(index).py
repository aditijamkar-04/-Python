def my_pop(lst,index):
    value=lst[index]
    new_lst=[]
    for i in lst:
        if i != value:
            new_lst.append(i)
    return value,new_lst


lst=[23,11,-22,56,12,67,-99,3]
index=4
print(my_pop(lst, index))