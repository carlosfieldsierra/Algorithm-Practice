'''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) – Push element x onto stack.
    pop() – Removes the element on top of the stack.
    top() – Get the top element.
    getMin() – Retrieve the minimum element in the stack.
    Note that all the operations have to be constant time operations.

    Questions to ask the interviewer :

    Q: What should getMin() do on empty stack? 
    A: In this case, return -1.

    Q: What should pop do on empty stack? 
    A: In this case, nothing. 

    Q: What should top() do on empty stack?
    A: In this case, return -1
'''

class MinStack:
    
    def __init__(self):
        self.size = 100
        self.stack = [0] * self.size 
        self.index = -1
        self.minElem = float('inf')
        
    
    def half(self):
        if self.size //2 < 100:
            return 
        self.size = self.size // 2
        newArray = [0] * self.size
        for i in range(self.size):
            newArray[i] = self.stack[i]
        self.stack = newArray 
        
    def double(self):
        self.size = self.size * 2
        newArray = [0] * self.size
        for i in range(len(self.stack)):
            self.stack[i] = newArray[i]
            
        self.stack = newArray 
    
    # @param x, an integer
    def push(self, x):
        self.index += 1 
        if self.index == self.size:
            self.double()
        
        self.minElem = min(self.minElem,x)
        self.stack[self.index] = x
        

    # @return nothing
    def pop(self):
        if self.index == -1: return
        
        if self.index < self.size //2:
            self.half()
        
        value = self.stack[self.index]
        self.index -=1 
        return value 


    # @return an integer
    def top(self):
        if self.index == -1: return -1
        return self.stack[self.index]


    # @return an integer
    def getMin(self):
        if self.index == -1: return -1
        return self.minElem
        



def solve(A):
    stack = MinStack()
    for elem in A:
        stack.push(elem)

    value = stack.pop()
    while value:
        print(value)
        value = stack.pop()
    print('--')
    for elem in A:
        stack.push(elem)
        print(elem,stack.stack)
    
    value = stack.pop()
    while value:
        print(value)
        value = stack.pop()

def Main():
    ans = solve([1,2,34,3,2,122,2])
    print(f"answer {ans}")

if __name__ == "__main__":
    Main()