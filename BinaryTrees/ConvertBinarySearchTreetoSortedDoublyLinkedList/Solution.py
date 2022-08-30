
class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        head,tail = None

        def dfs(node):
            nonlocal head,tail
            if not node:
                return None

            dfs(node.left)
            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node
            tail = node  
            dfs(node.right)

            return head
             

        

        dfs(root)  
        
        head.left  = tail
        tail.right = head

        return head


def Main():
    root = None # BST
    ans = Solution.treeToDoublyList(root)
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()