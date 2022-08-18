

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

def solve(root,target):

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.val == target:
            return True
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return False 

def solve2(root,target):
    return root.val == target \
        or solve2(root.left,target) \
        or solve2(root.right,target) \
        if root else False

def Main():
    root = getTreeOne()

    ans = solve(root,"e")
    print(f"\nAnswer: {ans}\n")

    ans = solve(root,"z")
    print(f"\nAnswer: {ans}\n")

    ans = solve2(root,"e")
    print(f"\nAnswer: {ans}\n")

    ans = solve2(root,"z")
    print(f"\nAnswer: {ans}\n")



    

if __name__ == "__main__":
    Main()