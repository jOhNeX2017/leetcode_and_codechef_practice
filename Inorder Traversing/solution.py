# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        res = []

        def traversing(node):
            if node:
                traversing(node.left)
                res.append(node.val)
                traversing(node.right)
        
        traversing(node)
        return res