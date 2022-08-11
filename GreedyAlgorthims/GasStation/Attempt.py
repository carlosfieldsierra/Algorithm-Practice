'''
    Given two integer arrays A and B of size N. There are N gas stations along a circular route, where the amount of gas at station i is A[i].
    You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

    Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.
    You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2.. Completing the circuit means starting at i and ending up at i again.
'''
# O(N^2) runtime | O(1) spacetime
def solve(A,B):
    n = len(A)
    
    for i in range(n):
        gas = A[i] - B[i]
        if gas < 0:
            continue
        
        # station-end
        for j in range(i+1,n):
            gas += A[j] - B[j]
            if gas < 0:
                gas = -1
                break
        
        if gas == -1:
            continue
        
        # start-station
        for j in range(0,i):
            gas += A[j] - B[j]
            if gas < 0:
                gas = -1
                break
            
        if gas != -1:
            return i
    
    return -1   
                



def Main():
    pass

if __name__ == "__main__":
    Main()
