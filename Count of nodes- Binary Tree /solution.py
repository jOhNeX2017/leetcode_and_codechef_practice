class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
    

# input is in preorder
inputs = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
# -1 means null/None

idx =-1

def buildTree(nodes) :
    global idx
    idx+=1
    
    if idx<len(nodes) and nodes[idx] == -1 :
        return None
    
    node = Node(nodes[idx])
    node.left = buildTree(nodes)
    node.right = buildTree(nodes)
    
    return node

root = buildTree(inputs)

# sum=0

def countNodes(node):
    if not node:
        return 0
    
    leftCount = countNodes(node.left)
    rightCount = countNodes(node.right)
    
    return leftCount+rightCount+1

print(countNodes(root))