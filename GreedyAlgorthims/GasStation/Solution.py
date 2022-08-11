'''
    Given two integer arrays A and B of size N. There are N gas stations along a circular route, where the amount of gas at station i is A[i].
    You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

    Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.
    You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2.. Completing the circuit means starting at i and ending up at i again.
'''



def solve(A,B):
    n = len(A)
    
    curr = start = 0

    for i, (g,c) in enumerate(zip(A*2,B*2)):
        if i == start + n:
            return start
        
        curr += g - c

        if curr < 0:
            start = i + 1
            curr = 0

    return -1
   



def Main():
    A = [3,5,2,1,7]
    B = [4,2,1,9,1]
    ans = solve(A,B) # 4
    
    print(f"Answer: {ans}")

if __name__ == "__main__":
    Main()