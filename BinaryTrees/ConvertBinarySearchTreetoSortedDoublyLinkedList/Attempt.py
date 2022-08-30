"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None
        data = []
        inOrder(root,data)
        if len(data) == 1:
            root.left = root
            root.right = root
            return root
        
        for i in range(len(data)-1):
            leftNode = data[i]
            rightNode = data[i+1]
            leftNode.right = rightNode
            rightNode.left = leftNode
        
        lastLeftNode,lastRightNode = data[0],data[-1]
        
        lastLeftNode.left = lastRightNode
        lastRightNode.right = lastLeftNode
        
        return lastLeftNode
            
        
            
        
        
        
def inOrder(root,data):
    if not root: return 
    inOrder(root.left,data)
    data.append(root)
    inOrder(root.right,data)
    