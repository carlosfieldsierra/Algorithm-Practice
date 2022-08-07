'''
    Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.
    Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.
    Return a integer denoting the length of maximal set of mutually disjoint intervals.
'''


# O(N^3) runtime | O(N^2) spacetime
def solve(matrix):
    
    matrix.sort(key=lambda a: a[0])
    answers = []
    
    for i in range(len(matrix)):
        answer = [ matrix[i] ]
        for j in range(i+1,len(matrix)):
            elem = matrix[j]
            if isDisJoint(answer,elem):
                answer.append(elem)
        answers.append(answer)

    
    return max([len(ans) for ans in answers])
            
            
def isDisJoint(answer,elem):
    for ans in answer:
        if not isDisJointPair(ans,elem):
            return False
    return True

def isDisJointPair(A,B):
    a1,a2 = A
    b1,b2 = B
    return a1 < b1 and a2 < b2 and a2 < b1



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