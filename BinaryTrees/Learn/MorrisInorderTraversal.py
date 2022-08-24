

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morrisTraversal(root):
    curr = root

    while not curr:
        if not curr.left:
            print(curr.val) # Visit
            curr = curr.right
        else:
            predecessor = findPredecessor(curr)
            if not curr.right:
                findPredecessor.right = curr
                curr = curr.left
            else:
                predecessor.right = None
                print(curr.val) # Visit
                curr = curr.right


'''
One left, right as possible
'''
def findPredecessor(curr):
    pass 