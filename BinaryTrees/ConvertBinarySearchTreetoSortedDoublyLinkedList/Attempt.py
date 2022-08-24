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
        
        leftNode  = toDoubleLinkedList(root.left)
        rightNode  = toDoubleLinkedList(root.right)

        leftNode_lastLeft = getLastLeftNode(leftNode)
        leftNode_lastRight = getLastRightNode(leftNode)
        
        rightNode_lastRight = getLastRightNode(rightNode)
        rightNode_lastLeft = getLastLeftNode(rightNode)

        if not leftNode and not rightNode:
            return root
        elif not leftNode:
            root.right = rightNode_lastLeft
            rightNode_lastLeft.left = root
            
            root.left =  rightNode_lastRight
            rightNode_lastRight.right = root
    
            return root
            
        elif not rightNode:
            
            root.right = leftNode_lastLeft
            leftNode_lastLeft.left = root
            
            leftNode_lastRight.right = root
            root.left = leftNode_lastRight
        else:
            leftNode_lastRight.right = root
            root.right = rightNode_lastLeft
            
            leftNode_lastLeft.right = rightNode_lastRight
            rightNode_lastRight.left = leftNode_lastLeft
            
            return leftNode_lastLeft


        

def getLastRightNode(node):
    if not node:
        return None
    
    while node.right != None:
        node = node.right
    
    return node
    
def getLastLeftNode(node):
    if not node:
        return None
    
    while node.left != None:
        node = node.left 
    
    return node 
    
    
def toDoubleLinkedList(node):
    if not node:
        return None
    
    # Left Node
    leftNode = toDoubleLinkedList(node.left)
    node.left = leftNode
    if leftNode:
        leftNode.right = node
    # Right Node
    rightNode = toDoubleLinkedList(node.right)
    node.right = rightNode
    if rightNode:
        rightNode.left = node
    
    return rightNode if rightNode else node 

   
    
   
        