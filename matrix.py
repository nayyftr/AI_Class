import numpy as np

A = [[2, 0, -3], 
    [1, 4, 5]]

B = [[3, 1], 
    [-1, 0], 
    [4, 2]]

C = [[4, 7], 
    [2, 1], 
    [1, -1]]

def multiply_matrices_manual(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def add_matrices_manual(mat1, mat2):
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

def multiply_matrices_numpy(mat1, mat2):
    return np.dot(mat1, mat2)

def add_matrices_numpy(mat1, mat2):
    return np.add(mat1, mat2)

method = 'numpy' 

if method == 'numpy':
    A_np = np.array(A)
    B_np = np.array(B)
    C_np = np.array(C)
    
    AB = multiply_matrices_numpy(A_np, B_np)
    AC = multiply_matrices_numpy(A_np, C_np)
    result = add_matrices_numpy(AB, AC)
    print("Menggunakan numpy:")
    print(result)
    
elif method == 'manual':
    AB = multiply_matrices_manual(A, B)
    AC = multiply_matrices_manual(A, C)
    result = add_matrices_manual(AB, AC)
    print("Menggunakan metode manual:")
    for row in result:
        print(row)
