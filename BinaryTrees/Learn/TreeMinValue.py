

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def getTreeOne():
    '''
            3
           / \
          11  4
         / \   \
        4   2   1
    '''
    a = Node(3)
    b = Node(11)
    c = Node(4)
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
    ans = float('inf')
    queue = [root]
    while queue:
        node = queue.pop(0)
        ans = min(node.val,ans)
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)




    return ans 

def solve2(root):
    if not root: return float('inf')
    return min(min(root.val,solve2(root.left)),min(root.val ,solve2(root.right)))

def Main():
    root = getTreeOne()

    ans = solve(root)
    print(f"\nAnswer: {ans}\n")

    ans = solve2(root)
    print(f"\nAnswer: {ans}\n")

  

    

if __name__ == "__main__":
    Main()