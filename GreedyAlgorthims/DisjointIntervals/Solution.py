'''
    Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.
    Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.
    Return a integer denoting the length of maximal set of mutually disjoint intervals.
'''

# O(N*LOG(N)) runtime | O(1) spacetime 
def solve(A):
    A.sort(key=lambda a:a[1])
    
    _, prev_e = A[0]
    count = 1
    for s, e in A:
        if s > prev_e: 
            _, prev_e = s, e
            count+=1
 
    return count




def Main():
    matrix = [
        [4, 4],
        [8, 15],
        [6, 6],
        [2, 13],
        [2, 12]
    ]

    print(solve(matrix))

if __name__ == "__main__":
    Main()


