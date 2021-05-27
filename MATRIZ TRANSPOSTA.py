#Recebe o número de linhas e colunas de uma matriz e calcula sua transposta
L = int(input('Digite o número de linhas da matriz A: '))
C = int(input('Digite o número de colunas da matriz A: '))

A = [[0 for x in range(L)] for y in range(C)]
B = [[0 for i in range(C)] for j in range(L)]


def preencheMatriz():
    print('Digite os valores para preencher sua Matriz:')
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(input())
    print('Matriz A:', A)

def transposeMatriz():
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]
    print('Matriz A transposta:', B)

preencheMatriz()
transposeMatriz()
