import numpy as np

def read_input(file_name):
    with open(file_name, "r") as file:
        m, n = map(int, file.readline().split())
        preferences = {}
        for i in range(m):
            prefs = list(map(int, file.readline().split()[1:]))
            preferences[i + 1] = prefs

        k = int(file.readline())
        conflicts = set(tuple(map(int, file.readline().split())) for _ in range(k))

        return m, n, preferences, conflicts
    
def create_matrix(m, n, preferences, conflicts):
    A = []
    for i in range(1, m + 1):
        tmp = []
        for j in range(n):
            if (j + 1) in preferences[i]:
                tmp.append(1)
            else:
                tmp.append(0)
        A.append(tmp)

    B = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if ((i + 1, j + 1) in conflicts) or ((j + 1, i + 1) in conflicts):
                tmp.append(1)
            else:
                tmp.append(0)
        B.append(tmp)

    return np.array(A), np.array(B)

def write_output(results, file_name):
    m, n = results.shape
    with open(file_name, 'w') as f:
        # Write the number of courses
        f.write(str(n) + '\n')
        # Find the teacher for each course
        teachers = [i + 1 for j in range(n) for i in range(m) if results[i, j] == 1]
        f.write(' '.join(map(str, teachers)) + '\n')
