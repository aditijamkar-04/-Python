def merge_sort(lst, low, high):
    if low == high:   # base case: single element
        return [lst[low]]
    
    mid = (low + high) // 2
    left_lst = merge_sort(lst, low, mid)
    right_lst = merge_sort(lst, mid + 1, high)
    return merging(left_lst, right_lst)

def merging(lst1, lst2):
    i = j = 0
    result = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    while i < len(lst1):
        result.append(lst1[i])
        i += 1
    while j < len(lst2):
        result.append(lst2[j])
        j += 1
    return result

# Test Data
lst = [23, 11, -22, 56, 12, 67, -99, 3]
low = 0
high = len(lst) - 1

print(merge_sort(lst, low, high))