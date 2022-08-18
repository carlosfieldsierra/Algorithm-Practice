class Solution:
    def invertTree(self, root):
        invert(root)
        return root 
    
    
    
def invert(root):
    if root == None:
        return None
    
    prevRootLeft = root.left
    root.left  = invert(root.right)
    root.right = invert(prevRootLeft)
    
    return root