import numpy as np

def check_conflicts(results, i, j, B):
    for k in range(len(results[i])):
        if results[i, k] == 1 and B[j, k] == 1:
            return False
    return True

def max_load(A):
    return max(sum(A[i]) for i in range(len(A)))

def greedy_algorithm(A, B):
    n = len(A[0])
    m = len(A)
    results = np.zeros_like(A)
    for j in range(n):
        tmp_results = []
        for i in range(m):
            tmp_result = np.copy(results)
            if A[i, j] == 1 and check_conflicts(results, i, j, B):
                tmp_result[i, j] = 1
                tmp_results.append(tmp_result)

        tmp_max_load = float('inf')
        for tmp_result in tmp_results:
            if max_load(tmp_result) < tmp_max_load:
                results = np.copy(tmp_result)  
                tmp_max_load = max_load(tmp_result)
    
    return results, max_load(results)

def hill_climbing(A, B):
    n = len(A[0])
    m = len(A)

    results = np.zeros_like(A)
    for j in range(n):
        for i in range(m):
            if A[i, j] == 1 and check_conflicts(results, i, j, B):
                results[i, j] = 1
                break

    while True:
        neighbor_found = False
        current_max_load = max_load(results)
        for j in range(n):
            for i in range(m):
                if A[i, j] == 1 and results[i, j] == 0 and check_conflicts(results, i, j, B):
                    results_copy = results.copy()
                    results_copy[:, j] = 0
                    results_copy[i, j] = 1
                    if max_load(results_copy) < current_max_load:
                        results = results_copy
                        neighbor_found = True
                        break
            if neighbor_found:
                break
        if not neighbor_found:
            break

    return results, max_load(results)

def backtracking_algorithm(A, B, results=None, j=0, current_max_load=0):
    n = len(A[0])
    m = len(A)

    if results is None:
        results = np.zeros_like(A)

    if j == n:
        return results, current_max_load

    for i in range(m):
        if A[i, j] == 1 and check_conflicts(results, i, j, B):
            results[i, j] = 1
            new_max_load = max(current_max_load, sum(results[i]))

            res = backtracking_algorithm(A, B, results, j + 1, new_max_load)
            if res is not None:
                return res

            results[i, j] = 0

    return None