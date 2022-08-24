# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        temp = []
        inOrder(root,temp)

        srt = sorted(n.val for n in temp)
        
        for i in range(len(srt)):
            temp[i].val = str[i]

def inOrder(root,temp):
    if not root: return

    inOrder(root.left)
    temp.append(root)
    inOrder(root.right)