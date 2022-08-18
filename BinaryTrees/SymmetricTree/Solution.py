'''
    101. Symmetric Tree

    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    

    Example 1:


    Input: root = [1,2,2,3,4,4,3]
    Output: true
    Example 2:


    Input: root = [1,2,2,null,3,null,3]
    Output: false
    

    Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

'''
class Node:
    def __init__(self,value):
        self.val = value
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


def isSymmetric(root):
    return isMirror(root.left,root.right)

def isMirror(left_node,right_node):
    if not left_node and not right_node:
        return True 
    if not left_node or not right_node:
        return False 

    return left_node.val == right_node.val \
        and isMirror(left_node.left,right_node.right) \
        and isMirror(left_node.right,right_node.left)
def Main():
    ans = isSymmetric(getTreeOne())
    print(f"\nAnswer: {ans}\n")
    


if __name__ == "__main__":
    Main()