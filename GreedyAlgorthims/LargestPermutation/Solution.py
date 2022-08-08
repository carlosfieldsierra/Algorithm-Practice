'''
    Given an integer array A of size N consisting of 
    unique integers from 1 to N. You can swap any 
    two integers atmost B times.

    Return the largest lexicographical value array 
    that can be created by executing atmost B swaps.
'''


def solve(A,B):
    numToIndexMap = {num: i for i,num in enumerate(A)}

    index = 0
    curMaxValue = len(A)

    while B and  index < len(A):
        
        maxValIndex = numToIndexMap[curMaxValue]

        if maxValIndex != index:
            # Flip Array
            A[maxValIndex],A[index] = A[index], A[maxValIndex]
    
            # Flip Dictionary
            numToIndexMap[A[maxValIndex]],numToIndexMap[A[index]] = \
                numToIndexMap[A[index]], numToIndexMap[A[maxValIndex]]
            B -= 1 
            
            
        index += 1
        curMaxValue -= 1
        
    
    return A
   
  
        

         
def Main():
    ans = solve([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ],4)
    print(ans)

if __name__ == "__main__":
    Main()