def my_remove(lst, element):
    new_lst=[]
    for ele in lst:
        if ele!=element:
            new_lst.append(ele)
    return new_lst


lst=[23,11,-22,56,12,67,-99,3]
element=11
print(my_remove(lst, element))