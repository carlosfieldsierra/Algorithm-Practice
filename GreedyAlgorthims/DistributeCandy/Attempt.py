'''
    There are N children standing in a line. Each child is assigned a rating value.

    You are giving candies to these children subjected to the following requirements:

    1. Each child must have at least one candy.
    2. Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?
'''


'''     
    Error only works for non  flat regions 
    or plateus, no neighbors
'''


def solve(A):

    # O(N)
    peaks = [isPeak(A,i) for i in range(len(A))]
    
    # O(N)
    flats = [isFlat(A,i) for i in range(len(A))]
    
    # O(N)
    peakHeightsForwards = [0]*len(A)
    count = 1
    for i in range(len(A)):
        index = i
        if peaks[index]:
            peakHeightsForwards[index] = count
            count = 1
        else:
            count+=1

    # O(N)
    peakHeightBackwards = [0]*len(A)
    count = 1
    lastIndex = len(A)-1
    for i in range(len(A)):
        index = lastIndex-i
        if peaks[index]:
            peakHeightBackwards[index] = count
            count = 1
        else:
            count+=1

    
    # O(N)
    peakHeights = [
        max(peakHeightBackwards[i],peakHeightsForwards[i]) \
            for i in range(len(A))
        ]

    # O(N)
    candies = 0
    for height in peakHeights:
        candies += height + guassSum(height-1)

    return int(candies)
    
    


def isFlat(array,index):
    # The value
    value = array[index]

    # First index
    if index == 0:
        next = array[index+1]
        return value == next and not isPeak(array,index+1)
    # Last index
    if index == len(array)-1:
        prev = array[index-1]
        return value == prev and not isPeak(array,index-1)

    prev , next = array[index-1],array[index+1]

    return (value==prev and not isPeak(array,index-1)) or \
        (value==next and not isPeak(array,index+1))

            
def isPeak(array,index):
    # The value
    value = array[index]

    # First index
    if index == 0:
        next = array[index+1]
        return value > next
    # Last index
    if index == len(array)-1:
        prev = array[index-1]
        return value > prev

    prev , next = array[index-1],array[index+1]

    return value > prev and value > next


def guassSum(n):
    return (n*(n+1))/2

def Main():
    
    A = [5,3,6,5,4,3,2]

    ans = solve(A)

    print(ans)

if __name__ == "__main__":
    Main()