# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
            Do not return anything, modify root in-place instead.
        """
        arr = []
        # O(N)
        inOrder(root,arr)
        
        print([i.val for i in arr])
        pair = []
        for i in range(len(arr)):
            if i != 0 and arr[i-1].val > arr[i].val:
                pair.append(arr[i])
            
            if i != len(arr)-1 and arr[i].val < arr[i+1].val:
                pair.append(arr[i])
        
        
        node_one,node_two = pair
        
        node_one_l_child = node_one.left
        node_one_r_child = node_one.right
        
        node_two_l_child = node_two.left
        node_two_r_child = node_two.right
        
        
        node_one.left = node_two_l_child
        node_one.right = node_two_r_child
        
        node_two.left = node_one_l_child
        node_two.right= node_one_r_child
        
        
        

        
def inOrder(root,arr):
    if root == None: return
    
    inOrder(root.left,arr)
    arr.append(root)
    inOrder(root.right,arr)
    
        
        