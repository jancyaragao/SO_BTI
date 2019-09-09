import os
import random
import threading

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

def unroll(args, func, method, results):
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
        print("\n")
        args[0] = results
        args.remove(args[1])
        sem.release()
        if len(args) > 1:
            unroll(args, func, method, results)
    else: 
        processos = []

        for arg, row_aleatoria in zip(matrix1, matrix2):
            processos.append([])
            func(arg, row_aleatoria, results)            

        print_matrix(results)

if __name__ == '__main__':
    res = []
    matrix1 = [[0,1,2],[3,4,5],[6,7,8]]
    matrix2 = [[8,7,6],[5,4,3],[2,1,0]]
    matrix3 = [[0,1,2],[3,4,5],[6,7,8]]
    matrix4 = [[8,7,6],[5,4,3],[2,1,0]]
    # unroll([matrix1,matrix2], process_multiply, 'proc', res)
    unroll([matrix1,matrix2,matrix3,matrix4], thread_mult, 'thre', res)
