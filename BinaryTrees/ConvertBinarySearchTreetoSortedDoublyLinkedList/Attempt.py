"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        

        leftNode  = toDoubleLinkedList(root.left)
        rightNode  = toDoubleLinkedList(root.right)

        leftNode_lastLeft = getLastLeftNode(leftNode)
        leftNode_lastRight = getLastRightNode(leftNode)
        
        rightNode_lastRight = getLastRightNode(rightNode)
        rightNode_lastLeft = getLastLeftNode(rightNode)

        if not leftNode and not rightNode:
            return root
        elif not leftNode:
            node.right = rightNode_lastLeft
            rightNode_lastLeft.left = node
            
            node.left =  rightNode_lastRight
            rightNode_lastRight.right = node
    
            return node
            
        elif not rightNode:
            
            node.right = leftNode_lastLeft
            leftNode_lastLeft.left = node
            
            leftNode_lastRight.right = node
            node.left = leftNode_lastRight
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

   
    
   
        