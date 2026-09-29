# 1

lst=[1,2,3,4,[5,6,7,8]]
print(lst[4])
print(lst[4][2])


# 2

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    print(matrix[i])


# 3

for i in range (len(matrix)):
    for j in range (len(matrix[0])):
        print(matrix[i][j])


# 4

#WAP to sum of elements in matrix
def sums(matrix):
    summat=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            summat+=matrix[i][j]
    return summat
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(sums(matrix))

# 5

#WAP to find the trace of the matrix ---> sum of all diagonal element 
def trace(matrix):
    trace=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i==j:
                trace+=matrix[i][j]
    return trace

matrix=[[2,3,5],
        [7,8,9],
        [4,5,10]]
print(trace(matrix))

# 6
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(trace(matrix))

# 7

#WAP to search an element in matrix
def searching(matrix,element):
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==element:
                return True
    return False
matrix=[[2,3,5],[7,8,9],[4,5,10]]
element=int(input("element:"))
print(searching(matrix,element))