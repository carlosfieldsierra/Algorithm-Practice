'''
    N light bulbs are connected by a wire.
    Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
    Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
    You can press the same switch multiple times.
    Note : 0 represents the bulb is off and 1 represents the bulb is on.
'''


 
'''
    Semi Working Atempt one
'''
from queue import PriorityQueue
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        # Start PriorityQueue
        pq = PriorityQueue()
        
        # Fill the PQ
        for index in range(len(A)):
            arraySwitch = self.flip(A,index)
            numberOfOnes = sum(arraySwitch) 
            pq.put((-numberOfOnes,(0,arraySwitch)))

        visted = []
        while not pq.empty():
            numberOfOnes, move_array = pq.get()
            move,array = move_array
            if array in visted:
                continue
            visted.append(array)
            if -numberOfOnes == len(array):
                return  move + 1
            for index in range(len(array)):
                arraySwitch = self.flip(array,index)
                numberOfOnes = sum(arraySwitch) 
                pq.put((-numberOfOnes,(move+1,arraySwitch)))


    def flip(self,array,index):
        newArray = [0] * len(array)

        for i in range(len(array)):
            if i < index:
                newArray[i] = array[i]
            else:
                newArray[i]  = 0 if array[i] == 1 else 1
        return newArray
    
def Main():
    A =  [ 1,0,1 ]
    
    moves = Solution().bulbs(A)
    print(moves)

if __name__ == "__main__":
    Main()


