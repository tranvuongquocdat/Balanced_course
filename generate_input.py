import numpy as np

def generate_input(m, n, filename):
    np.random.seed(0)  # for reproducibility

    with open(filename, 'w') as file:
        # Write the number of teachers and courses
        file.write(f"{m} {n}\n")

        # For each teacher, write the courses they can teach
        for _ in range(m):
            courses = np.random.choice(n, size=np.random.randint(1, n+1), replace=False) + 1
            file.write(f"{len(courses)} {' '.join(map(str, courses))}\n")

        # Write the number of conflicting courses
        conflicts = np.random.choice(n*(n-1)//2, size=np.random.randint(1, n*(n-1)//2+1), replace=False) + 1
        file.write(f"{len(conflicts)}\n")

        # For each conflict, write the pair of conflicting courses
        for _ in range(len(conflicts)):
            pair = np.random.choice(n, size=2, replace=False) + 1
            file.write(f"{pair[0]} {pair[1]}\n")

generate_input(3, 10, 'input_2.txt')