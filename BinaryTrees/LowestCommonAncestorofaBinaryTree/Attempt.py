'''

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(N) runtime | O(N) spactime
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        p_parents = getParents(root,p)
        q_parents = getParents(root,q)
        
        if q in p_parents:
            return q
        if p in q_parents:
            return p
        
        parents = set()
        for parent in p_parents:
            parents.add(parent)
            
        for parent in reversed(q_parents):
            if parent in parents:
                return parent
        
    
    
def getParents(root,target):
    if root == None:
        return False
    if root == target:
        return []
    
    l = False
    r = False
    if root.left:  l = getParents(root.left,target)
    if root.right: r = getParents(root.right,target)
        
    if l!=False:
        return [root] + l
    if r!=False:
        return [root] + r
    
    return False