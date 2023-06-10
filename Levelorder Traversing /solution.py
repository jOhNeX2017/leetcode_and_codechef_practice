# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        res = []


        def traversing(node):
            if node:
                
                if node.left:
                    res.append(node.left.val)
                
                if node.right:
                    res.append(node.right.val)
                
                traversing(node.left)
                traversing(node.right)
        
        res.append(node.val)
        traversing(node)
        return res
    
    def levelorderTraversalwithPrintInLevel(self, node: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not node:
            return
        
        res.add(node)
        res.add(None)
        
        while(len(res)>0):
            if not res[0] :
                print("")
                if len(res) ==0:
                    break
                else:
                    res.append(None)
            else:
                currNode = res[0]
                
                if currNode.left:
                    res.append(currNode.left)
                
                if currNode.right:
                    res.append(currNode.right)
                
                print(currNode.val,end=" ")
                res.pop(0)