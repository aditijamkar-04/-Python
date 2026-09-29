#1
#wAP to find a matrix is scalar matrix
def is_square(matrix):
    return len(matrix) == len(matrix[0])

def is_scalar(matrix):
    if not is_square(matrix):
        return False
    
    diagonal_value = matrix[0][0]  # reference diagonal element
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                if matrix[i][j] != diagonal_value:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

matrix=[[2,3,5],
        [7,8,9],
        [4,5,10]]
print(is_scalar(matrix))


matrix=[[2,0,0],
        [0,2,0],
        [0,0,2]]
print(is_scalar(matrix))


#2
#WAP to check a matrix is a upper triangular matrix or not
def upper_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Check elements below the main diagonal
            if i > j and matrix[i][j] != 0:
                return False
    # Only return True after checking the entire matrix
    return True

matrix = [[2, 3, 5],
          [7, 8, 9],
          [4, 5, 10]]
print(upper_triangular(matrix)) 


matrix=[[2,3,5],
        [0,8,9],
        [0,0,10]]
print(upper_triangular(matrix)) 


#3
#WAP to check a matrix is a Lower triangular matrix or not
#WAP to check a matrix is lower triangle
def lower_triangular(matrix):
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i<j and matrix[i][j]!=0:
                    return False
    return True

matrix=[[2,3,5],
        [7,8,9],
        [4,5,10]]
print(lower_triangular(matrix)) 


#4
#WAP to addition of two matrix
def addition(m1,m2):
    result=[[0,0],[0,0]]
    for i in range (len(m1)):
        for j in range(len(m1[0])):
            result[i][j]=m1[i][j]+m2[i][j]
    return result

m1=[[2,3,],
    [5,6]]
m2=[[1,2],
    [3,1]]
print(addition(m1,m2))


#5
# Transpose of matrix
def transpose(matrix):
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            if i<j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix

matrix=[[2,3,5],
        [7,8,9],
        [4,5,10]]
print(transpose(matrix))


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))


