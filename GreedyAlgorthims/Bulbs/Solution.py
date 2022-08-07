'''
    N light bulbs are connected by a wire.
    Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
    Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
    You can press the same switch multiple times.
    Note : 0 represents the bulb is off and 1 represents the bulb is on.
'''



'''
    Naive Solution
'''
# O(N^2) runtime | O(1) spacetime
def naiveSolution(array):
    cost = 0
    for i in range(len(array)):
        if array[i] == 0:
            cost += 1
            flip(array,i)
    
    return cost

def flip(array,index):
    for i in range(index,len(array)):
        array[i] = 1 if array[i] == 0 else 0

'''
    Optimized Solution
'''
def solution(array):
    pass 

def Main():
    print(naiveSolution([0,1,0,1]))

if __name__ == "__main__":
    Main()