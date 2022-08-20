'''
    366. Find Leaves of Binary Tree
    Medium

    Given the root of a binary tree, collect a tree's nodes as if you were doing this:

    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.
    

    Example 1:


    Input: root = [1,2,3,4,5]
    Output: [[4,5,3],[2],[1]]
    Explanation:
    [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
    Example 2:

    Input: root = [1]
    Output: [[1]]
    

    Constraints:

    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100
    Accepted
    210,159
    Submissions

'''

# O(N) runtime | O(N) spactime  
def solve(root):
    if not root:
        return []
    
    ans = []
    
    
    def dfs(root):
        if root == None:
            return 0
        
        depth = 1 + max(dfs(root.left),dfs(root.right))
        
        if depth -1 == len(ans):
            ans.append([])
        
        ans[depth].append(root.val)
        
        return depth
    
    dfs(root)
    
    return ans

def Main():
    root = None # A binary tree
    ans = solve(root)

    print(f"\nAnswer: {ans}\n")


if __name__ == "__main__":
    Main()


