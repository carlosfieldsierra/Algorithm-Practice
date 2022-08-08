'''
    Given an integer array A of size N consisting of 
    unique integers from 1 to N. You can swap any 
    two integers atmost B times.

    Return the largest lexicographical value array 
    that can be created by executing atmost B swaps.
'''

def solve(A,B):
   i = 0
   _max = len(A)
   d = {x:i for i,x in enumerate(A)}

   while B and i < len(A):
        j = d[_max] # Get index of value
        if i != j:
            B -= 1
            A[i], A[j] = A[j], A[i]
            
         
def Main():
    solve([4,8,2,7,1],2)

if __name__ == "__main__":
    Main()