

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def getTreeOne():
    '''
            5
           / \
          11  3
         / \   \
        4   2   1
    '''
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    
    return a

def solve(root):
    pass 

def solve2(root):
    if not root:
        return 0
    
    return root.val + max(
        solve2(root.left),solve2(root.right)
    ) 

    



def Main():
    root = getTreeOne()

    ans = solve(root)
    print(f"\nAnswer: {ans}\n")

    ans = solve2(root)
    print(f"\nAnswer: {ans}\n")

  

    

if __name__ == "__main__":
    Main()