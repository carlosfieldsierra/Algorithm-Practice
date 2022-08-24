



class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def getTree():
    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    root.left = two
    root.right = three
    three.left = four
    three.right = five

    return root


def serialize( root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    
    data = []
    def createData(node,data):
        if not node: 
            data+= "N"
            return

        data += f"{node.val}"
        createData(node.left,data)  
        createData(node.right,data)
    
    createData(root,data)

    return ",".join(data)
    
    
    

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """

    vals = data.split(",")
    class I:
        def __init__(self):
            self.val = 0

        def add(self):
            self.val+=1
        
        def get(self):
            return self.val
            
    i = I()
    def dfs():
        if i.get() > len(vals) -1 :
            return None
        if vals[i.get()] == "N":
            return  None
        
        node = TreeNode(int(vals[i.get()]))
        i.add()
        node.left = dfs()
        i.add()
        node.right = dfs()
        return node 
    
    return dfs()
    




def Main():
    root = getTree()
    data = serialize(root)
    print(f"\nData: {data}\n")
    sameRoot =  deserialize(data)
    print(serialize(sameRoot))


if __name__ == "__main__":
    Main()