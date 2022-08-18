'''
    Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.

    

    Example 1:


    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
    Example 2:

    Input: root = [1,2]
    Output: 1
    

    Constraints:

    The number of nodes in the tree is in the range [1, 104].
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



def diameterOfBinaryTree(root):
    res =  [0]

    def dfs(root):
        if not root:
            return -1
        
        left  = dfs(root.left)
        right = dfs(root.right)

        res[0] = max(2 + left + right,res[0])
 
        return 1 + max(left,right)


    dfs(root)
    return res[0] 

def Main():
    ans = diameterOfBinaryTree(getTreeOne())
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()  

