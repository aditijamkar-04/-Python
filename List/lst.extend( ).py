# extend()--->it is used to merge a two list

def merging_two_lst(lst1,lst2):
    i=j=0
    result=[] 
    while i<len(lst1) and j<len(lst2):
        if lst1[i]<lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
    if i==len(lst1):
        while j<len(lst2):
            result.append(lst2[j])
            j+=1 
    if j==len(lst2):
        while i<len(lst1):
            result.append(lst1[i])
    return result


lst1=[4,5,6,7,8,9]
lst2=[10,15,17,18]
print(merging_two_lst(lst1,lst2))