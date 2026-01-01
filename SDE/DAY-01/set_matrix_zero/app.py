matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]


def set_row(i, matrix):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0 :
            matrix[i][j] = -1
            
def set_col(j, matrix):
    for i in range(len(matrix)):
        if matrix[i][j] != 0 :
            matrix[i][j] = -1

def set_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -1 :
                matrix[i][j] = 0

def set_matrix_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 :
                set_row(i, matrix)
                set_col(j, matrix)
    
    set_matrix(matrix)
    
set_matrix_zero(matrix)
    
print(matrix)