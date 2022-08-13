'''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) - Push element x onto stack.
    pop() - Removes the element on top of the stack.
    top() - Get the top element.
    getMin() - Retrieve the minimum element in the stack.
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
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)

        if self.min_stack:
            self.min_stack.append(
                min(x,self.min_stack[-1])
            )
        else:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1] 
        return -1
    # @ret  urn an integer
    def getMin(self):
        if self.stack:
            return self.min_stack[-1]
        return -1

  


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
    
    value = stack.pop()
    while value:
        print(value)
        value = stack.pop()

def Main():
    ans = solve([1,2,34,3,2,122,2])
    print(f"answer {ans}")

if __name__ == "__main__":
    Main()