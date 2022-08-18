

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


def depthFirstValues(root):
    if not root: return []
    ans = []
    stack = [root]
    while stack:
        node = stack.pop()
        ans.append(node.val)

        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    
    return ans

    
def rdf(root):
    if not root: 
        return []
    
    ans = [root.val]
    if root.left: ans += rdf(root.left)
    if root.right: ans += rdf(root.right)

    return ans

    

    
    
   


def Main():
    root = getTreeOne()

    ans = depthFirstValues(root)
    print(f"\nAnswer: {ans}\n")
    ans = rdf(root)
    print(f"\nAnswer: {ans}\n")


    

if __name__ == "__main__":
    Main()