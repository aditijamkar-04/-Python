# Function to copy elements from one list to another
def copying(lst, empty_lst):
    for item in lst:
        empty_lst.append(item)
    return empty_lst

# Test Data
lst1 = [3, 4, 4, 5, 6, 7, 7, 7, 8, 9, 15]
lst2 = []

print(copying(lst1, lst2))