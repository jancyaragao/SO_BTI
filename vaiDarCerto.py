import os
import random
import threading

sem = threading.Lock()
def random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append([])
            matrix[i][j] = random.randint(0, 9)
    return matrix

# def sum_proc(row_a, row_b, results):
#     pid = os.fork() 
#     if pid == 0: 
#         aux = [] 
#         for a,b in zip(row_a, row_b):
#             aux.append(a + b)

#         results.append(aux)  

def sum_thre(i, j, a, b, results):
    threading.currentThread() 
    results[i][j] = a + b

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()

def unroll(args, func, method, results):
    random_m = random_matrix(len(args), len(args[0]))
    print("Matriz Original")
    print_matrix(args)
    print("Matriz radom\n")
    print_matrix(random_m)

    if method == "thre":
        threads = []
        cols = len(args[0])
        rows = len(args)

        results = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                threads.append([])
                threads[-1] = threading.Thread(target=func, args=(i, j, args[i][j], random_m[i][j], results))
                threads[-1].start()
        for i in range(rows):
            for j in range(cols):
                # threads.append([])
                # threads[-1] = threading.Thread(target=func, args=(i, j, args[i][j], random_m[i][j], results))
                threads[i+j].join()
        sem.acquire() 
        print("Matriz Resultante\n")     
        # res = results
        print_matrix(results)
        sem.release()

    else: 
        for arg, rand in zip(args, random_m):
            func(arg, rand, results)            

        print_matrix(results)

if __name__ == '__main__':
    res = []
    # unroll([[0,1,2],[3,4,5],[6,7,8]], sum_proc, 'proc', res)
    unroll([[0,1,2],[3,4,5],[6,7,8]], sum_thre, 'thre', res)
    print_matrix(res)