'''
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

    A leaf is a node with no children.

    

    Example 1:


    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path with the target sum is shown.
    Example 2:


    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There two root-to-leaf paths in the tree:
    (1 --> 2): The sum is 3.
    (1 --> 3): The sum is 4.
    There is no root-to-leaf path with sum = 5.
    Example 3:

    Input: root = [], targetSum = 0
    Output: false
    Explanation: Since the tree is empty, there are no root-to-leaf paths.
    

    Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
    Accepted
    956,688
    Submissions
'''
class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None 

def getTreeOne():
    '''
            5
           / \
          11  3
         / \   \
        4   2   1
    '''
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    
    return a

# O(N) runtime | O(LOG(N)) spacetime
def solve(root,targetSum):
    def dfs(node,curSum):
        if not node:
            return False
        
        curSum += node.val
        if not node.left and not node.right:
            return curSum == targetSum
        
        return dfs(node.left,curSum) or dfs(node.right,curSum)
    
    return dfs(root,0)



def Main():
    ans = solve(getTreeOne(),9)  # True
    print(f"\nAnswer: {ans}\n")  
    
    ans = solve(getTreeOne(),69) # False 
    print(f"\nAnswer: {ans}\n") 


if __name__ == "__main__":
    Main()