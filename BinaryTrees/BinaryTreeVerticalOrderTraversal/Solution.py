# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        
        levelToNodeMap = {}
        indexes = []
        queue = [(root,0)]
        while queue:
            node,level = queue.pop(0)
            if level not in levelToNodeMap:
                levelToNodeMap[level] = []
            levelToNodeMap[level].append(node.val)
            
            if node.left: queue.append((node.left,level-1))
            if node.right: queue.append((node.right,level+1))
        
        keys = sorted(levelToNodeMap.keys())
        return [levelToNodeMap[i] for i in keys ]
            