'''
    Given an integer array A of size N consisting of 
    unique integers from 1 to N. You can swap any 
    two integers atmost B times.

    Return the largest lexicographical value array 
    that can be created by executing atmost B swaps.
'''
 
    
def solve(A, B):
    
    sortedArray = A[:]
    sortedArray.sort(reverse=True)
    if B >= len(A):
        return sortedArray
    # O(N^2)
    cost = 0
    while cost!=B and cost < len(A):
        if A[cost] != sortedArray[cost]:
            i = cost
            oldIndex = A.index(sortedArray[i])
            A[i],A[oldIndex] = A[oldIndex], A[i]
                    
    return A


def Main():
    A = [4,8,2,7,1]
    print(solve(A,2))

if __name__ == "__main__":
    Main()