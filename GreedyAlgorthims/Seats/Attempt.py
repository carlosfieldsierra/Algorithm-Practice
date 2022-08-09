'''
    There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.
    An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
    Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.
    Return minimum value % MOD where MOD = 10000003
'''

def solve(A):
    cost = 0
    diff = 0
    firstSeatIndex = getFirstSeatIndex(A)
    for i in range(firstSeatIndex+1,len(A)):
        if A[i] == 'x':
            cost += diff
            diff = 0
        else:
            diff +=1
    
    return cost


def getFirstSeatIndex(A):
    for i in range(len(A)):
        if A[i] == 'x':
            return i

def Main():
    # A = [".", ".", ".", ".", "x", ".", ".", "x", "x", ".", ".", ".", "x", ".", ".",] 
    A = ".x.x.x..x"
    
    ans = solve(A)
    print("Answer: ",ans)

if __name__ == "__main__":
    Main()