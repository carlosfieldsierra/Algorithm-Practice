'''
    108. Convert Sorted Array to Binary Search Tree


    Add to List

    Share
    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

    

    Example 1:


    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

    Example 2:


    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
    

    Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
'''



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.val}"

def solve(nums):
    
    def helper(l,r):
        if l > r:
            return None

        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left  = TreeNode(l,m-1)
        root.right = TreeNode(m+1,r)  
        return root

    return helper(0,len(nums) - 1)
    

def bfs(root):
    visted = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        visted.append(node)
        if node.left:
            queue.append(node.left)
        
        if node.right:  
            queue.append(node.right)
        

    return visted

def Main():
    ans = solve([-10,-3,0,5,9])
    print(f"\nAnswer: {bfs(ans)}\n")


if __name__ == "__main__":
    Main()