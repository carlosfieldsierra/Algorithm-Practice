

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def getTreeOne():
    '''
            a
           / \
          b   c
         / \   \
        d   e   f
    '''
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    
    return a

def bfs(root):
    ans = []
    queue = [root]
    while queue: 
        node = queue.pop(0)
        ans.append(node.val)
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return ans

def Main():
    root = getTreeOne()

    ans = bfs(root)
    print(f"\nAnswer: {ans}\n")
    # ans = rdf(root)
    # print(f"\nAnswer: {ans}\n")


    

if __name__ == "__main__":
    Main()