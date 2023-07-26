# Balanced_course
BALANCED COURSE ASSIGNMENT

At the beginning of the semester, the head of a computer science department D have to assign courses to teachers in a balanced way. The department D has m teachers T={1,2,...,m} and n courses C={1,2,...,n}. Each teacher t∈T has a preference list which is a list of courses he/she can teach depending on his/her specialization. We known a list of pairs of conflicting two courses that cannot be assigned to the same teacher as these courses have been already scheduled in the same slot of the timetable. The load of a teacher is the number of courses assigned to her/him. How to assign n courses to m teacher such that each course assigned to a teacher is in his/her preference list, no two conflicting courses are assigned to the same teacher, and the maximal load is minimal.
Input
The input consists of following lines
•	Line 1: contains two integer m and n (1≤m≤10, 1≤n≤30)
•	Line i+1: contains an positive integer k and k positive integers indicating the courses that teacher i can teach (∀i=1,…,m)
•	Line m+2: contains an integer k
•	Line i+m+2: contains two integer i and j indicating two conflicting courses (∀i=1,…,k)
Output
If there are solutions, then write:
•	Line 1: contains n (numer of courses)
•	Line 2: contains x1, x2, . . ., xn in which xi is the index of teacher (teachers are indexed 1, 2, . . ., m) assigned to course i (i = 1, 2, . . ., n)
Otherwise, there is no solution, then write -1 in line 1.
Example
Input
3 10
7 1 2 5 6 7 8 10 
3 4 5 8 
6 2 3 4 6 7 9 
9
1 3
1 4
2 6
3 6
3 8
5 9
6 9
8 9
9 10


Output
10
1 3 3 2 1 1 3 2 3 1 

