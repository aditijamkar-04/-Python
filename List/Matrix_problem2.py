#1
# sum_of_each_row

def sum_of_each_row(matrix):
    for i in range(len(matrix)):
        row_sum=0
        for j in range(len(matrix[i])):
            row_sum+=matrix[i][j]
        print(row_sum)

matrix=[[1,2,3],
        [5,6,7],
        [7,8,9]]
print(sum_of_each_row(matrix))


#2
# sum_of_each_column

def sum_of_each_col(matrix):
    for i in range(len(matrix)):        # for j in range(len(matrix)):
        col_sum=0
        for j in range(len(matrix[i])):    # for i in range(len(matrix[i])):
            col_sum+=matrix[j][i]          # col_sum+=matrix[i][j]
        print(col_sum)

matrix=[[1,2,3],
        [5,6,7],
        [7,8,9]]
print(sum_of_each_col(matrix))


#3
def Bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

lst=[5,1,4,2,8]
print(Bubble_sort(lst))


#4

# By the single loop
def Bubble_sort(lst):
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i = 0   # reset to start after a swap
        else:
            i += 1
    return lst

lst = [5, 1, 4, 2, 8]
print(Bubble_sort(lst))