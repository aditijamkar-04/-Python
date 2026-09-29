# insert() -->it is used to add the element at a given position
def my_insert(lst,index,element):
    new_lst=[0]*(len(lst)+1)
    for i in range(index):
        new_lst[i]=lst[i]
    new_lst[index]=element 
    for i in range(index,len(lst)):
        new_lst[i+1]=lst[i] 
    return new_lst 



lst10=[3,4,5,6,7,8,9]
index=3
element=1000
print(my_insert(lst10,index,element))