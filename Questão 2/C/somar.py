import os
import random
import threading
import datetime
sem = threading.Lock()
# def somar_proc(row_a, row_b, results):
#     pid = os.fork() 
#     if pid == 0: 
#         aux = [] 
#         for a,b in zip(row_a, row_b):
#             aux.append(a + b)

#         results.append(aux)  

def somar_thre(i, j, a, b, results):
    threading.currentThread() 
    results[i][j] = a + b

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()

def unroll(args, func, method, results,time):
    matrix1 = args[0]
    matrix2 = args[1]
    print("Primeira Matriz")
    print_matrix(matrix1)
    print("Segunda Matriz")
    print_matrix(matrix2)

    if method == "thre":
        threads = []
        cols = len(matrix1[0])
        rows = len(matrix1)
        results = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                threads.append([])
                threads[-1] = threading.Thread(target=func, args=(i, j, matrix1[i][j], matrix2[i][j], results))
                threads[-1].start()
        for i in range(rows):
            for j in range(cols):
                threads[i+j].join()
        sem.acquire() 
        print("Matriz Resultante")     
        print_matrix(results)
        fim = datetime.datetime.today()
        duracao = fim - time
        print("Duração da execução: ",duracao.total_seconds())
        sem.release()

    else: 
        for arg, rand in zip(matrix1,matrix2):
            func(arg, rand, results)            

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
    import datetime
    valor = int(input("Tamanho:"))
    inicio = datetime.datetime.today()
    matrix1 = random_matrix(valor,valor)
    matrix2 = random_matrix(valor,valor)
    res = []
    # unroll([matrix1,matrix2], somar_proc, 'proc', res)
    unroll([matrix1,matrix2], somar_thre, 'thre', res,inicio)
    print_matrix(res)