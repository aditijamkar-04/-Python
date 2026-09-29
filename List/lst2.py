# Divide and Conquuer Strategy
def min_max_DnC(lst,low,high):
    if low==high:
        min_ele=max_ele=lst[low]
        return min_ele,max_ele 
    elif high==low+1:
        if lst[low]>lst[high]:
            min_ele=lst[high]
            max_ele=lst[low] 
        else:
            min_ele=lst[low]
            max_ele=lst[high]
        return min_ele,max_ele 
    else:
        mid=(low+high)//2 
        left_min,left_max=min_max_DnC(lst,low,mid)
        right_min,right_max=min_max_DnC(lst,mid+1,high)
        original_min=smaller(left_min,right_min)
        original_max=bigger(left_max,right_max)
        return original_min,original_max
def bigger(a,b):
    if a>b:
        return a
    else:
        return b
def smaller(a,b):
    if a<b:
        return a
    else:
        return b


lst=[23,11,67,33,-45,-100,78,89,12,99,110]
low=0
high=len(lst)-1
print(min_max_DnC(lst,low,high))