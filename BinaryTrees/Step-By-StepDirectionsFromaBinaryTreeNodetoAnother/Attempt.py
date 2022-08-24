# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# O(N) runtime | O(N) spacetime
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if not root:
            return ""
        lca = getLCA(root,startValue,destValue)
        start = ""
        end = ""
        queue = [(lca,"")]
        while queue:
            node,path = queue.pop(0)
            
            if startValue == node.val: start = path 
            if destValue  == node.val: end = path
            
            if node.left: queue.append((node.left,path+"L"))
            if node.right: queue.append((node.right,path+"R"))
        
        if start: start = len(start) * "U"
            
        return start + end
        
def getLCA(root,p,q):
    if not root: return None
    if root.val in (p,q): return root
    
    l = getLCA(root.left,p,q)
    r = getLCA(root.right,p,q)
    
    return root if l and r else r or l
     