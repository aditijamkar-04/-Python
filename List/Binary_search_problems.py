#1

def binary_search(lst,key):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==key:
            return True
        elif key>lst[mid]:
            low=mid+1
        else:
            high=mid-1
    return False

lst=[1,2,4,5,8]
key=5
print(binary_search(lst,key))


print(binary_search([1,2,4,5,8],10))


#2

# using Recursion

def binary_search(lst,low,high,key):
    if low>high:
        return False
    mid=(low+high)//2
    if lst[mid]==key:
        return True
    elif key>lst[mid]:
        return binary_search(lst,mid+1,high,key)
    else:
        return binary_search(lst,high,mid-1, key)

    lst=[1,2,4,5,8]
key=15
low=0
high=len(lst)-1
print(binary_search(lst,low,high,key))