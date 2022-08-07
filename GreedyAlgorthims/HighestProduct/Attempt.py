'''
    Given an array A, of N integers A.
    Return the highest product possible by multiplying 3 numbers from the array.
    NOTE:  Solution will fit in a 32-bit signed integer.
'''

def maxp3(A):
    A.sort()

    # - * - * +
    firstOne  = A[0]
    secondOne = A[1]
    # + * + * +
    lastOne = A[len(A)-1]
    nextlastOne = A[len(A)-2]
    nextNextlastOne = A[len(A)-3]

    productOne = firstOne * secondOne * lastOne
    productTwo = lastOne * nextlastOne * nextNextlastOne

    return productOne if productOne > productTwo else productTwo


def Main():
    print(maxp3([-5,-2,-1,0,0,1,1,5]))

if __name__ == "__main__":
    Main()