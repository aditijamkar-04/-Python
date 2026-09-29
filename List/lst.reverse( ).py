# # reverse the list  

def reverse_lst(lst):
    i=0
    j=len(lst)-1
    while i<j:
        lst[i],lst[j]=lst[j],lst[i]
        i+=1
        j-=1
    return lst


lst=[45,11,45,25,17,9,15]
print(reverse_lst(lst))