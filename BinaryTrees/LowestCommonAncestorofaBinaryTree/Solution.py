
def lowestCommonAncestor(root, p, q):
        def dfs(root):
            if not root:
                return None
            
            if root == p or root == q:
                return root
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            return root if l and r else l or r
        
        return dfs(root)

def lowestCommonAncestor(root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q 