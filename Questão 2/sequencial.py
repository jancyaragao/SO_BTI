import datetime
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()
inicio = datetime.datetime.today()
matrix1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matrix2 = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
print("Primeira Matriz")
print_matrix(matrix1)
print("Segunda Matriz")
print_matrix(matrix2)
cols = len(matrix1[0])
rows = len(matrix1)
results = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        results[i][j] = matrix1[i][j] + matrix2[i][j]
print("Matriz Resultante")
print_matrix(results)
fim = datetime.datetime.today()
duracao = fim - inicio
print("duração da soma ", duracao)
inicio = datetime.datetime.today()
cols = len(matrix2[0])
rows = len(matrix2)
results = [[0 for i in range(cols)] for j in range(len(matrix1))]
for j in range(cols):
    row2 = []
    for i in range(rows):
        row2.append(matrix2[i][j])
    for id, arg in enumerate(matrix1):
        valor = 0
        for idx in range(len(arg)):
            valor += arg[idx] * row2[idx]
        results[id][j] = valor
print("Primeira Matriz")
print_matrix(matrix1)
print("Segunda Matriz")
print_matrix(matrix2)
print("Matriz Resultante")
print_matrix(results)
fim = datetime.datetime.today()
duracao = fim - inicio
print("duração da multiplicação ", duracao)