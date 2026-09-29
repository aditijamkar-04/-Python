# 1

def common_element(lst1,lst2):
    result=[]
    count=0
    for i in lst1:
        for j in  lst2:
            if i==j:
                count+=1
                result.append(i)
    return result,count 

lst1=[3,4,5,6,7,8,9]
lst2=[7,8,9,10,15]
print(common_element(lst1,lst2))


# 2

#WAP to find the difference of maximum and minimum element in the list
def diff_element(lst):
    max_val = max(lst)
    min_val = min(lst)
    return max_val - min_val


lst3=[3,4,5,6,7,8,9]
lst4=[7,8,9,10,15]
print("Difference in lst3:", diff_element(lst3))
print("Difference in lst4:", diff_element(lst4))