import os
import random
import threading
import datetime
sem = threading.Lock()

def process_multiply(row_a, row_b, results):
    pid = os.fork()
    if pid == 0:
        aux = []
        for a, b in zip(row_a, row_b):
            aux.append(a + b)

        results.append(aux)  

def thread_mult(i, j, a, b, results):
    threading.currentThread()
    aux = 0
    for idx in range(len(a)):
        aux += a[idx] * b[idx]
    
    results[i][j] = aux

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()

def unroll(args, func, method, results,time):
    matrix1 = args[0]
    matrix2 = args[1]
    print("Primeira Matriz")
    print_matrix(args[0])
    print("Segunda Matriz")
    print_matrix(matrix2)
    if method == "thre":
        threads = []
        cols = len(matrix2[0])
        rows = len(matrix2)
        results = [[0 for i in range(cols)] for j in range(len(matrix1))]
        for j in range(cols):
            row2 = []
            for i in range(rows):
                row2.append(matrix2[i][j])
            for idx, arg in enumerate(matrix1):
                threads.append([])
                threads[-1] = threading.Thread(target=func, args=(idx, j, arg, row2, results))
                threads[-1].start() 
        sem.acquire()
        print("Matriz Resultante")
        print_matrix(results)
        fim = datetime.datetime.today()
        duracao = fim-time
        print("Duração :", duracao.total_seconds())
        sem.release()
    else: 
        processos = []

        for arg, row_aleatoria in zip(matrix1, matrix2):
            processos.append([])
            func(arg, row_aleatoria, results)            

        print_matrix(results)
def random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append([])
            matrix[i][j] = random.randint(0,10)
    return matrix
if __name__ == '__main__':
    valor = int(input("Tamanho:"))
    inicio = datetime.datetime.today()
    res = []
    matrix1 = random_matrix(valor,valor)
    matrix2 = random_matrix(valor,valor)
    # unroll([matrix1,matrix2], process_multiply, 'proc', res)
    unroll([matrix1,matrix2], thread_mult, 'thre', res,inicio)
