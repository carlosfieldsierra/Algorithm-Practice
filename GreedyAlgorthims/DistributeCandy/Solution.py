'''
    There are N children standing in a line. Each child is assigned a rating value.

    You are giving candies to these children subjected to the following requirements:

    1. Each child must have at least one candy.
    2. Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?
'''


# O(N*LOG(N)) rumtime | O(N) spacetime
def solve(A):
    length = len(A)
    data = sorted((elem,index) for index,elem in enumerate(A))

    candies = [1] * length

    for _, i in data:
        if i > 0 and A[i] > A[i-1]:
            candies[i] = candies[i-1]+1
    
        if i < length -1 and A[i] > A[i+1]:
            candies[i] = max(candies[i],candies[i+1]+1)

    return sum(candies)




def Main():
    A = [1,7,4,3]

    ans = solve(A)

    print(ans)


  




if __name__ == "__main__":
    Main()