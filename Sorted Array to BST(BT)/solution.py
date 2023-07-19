# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def add_node(left,right,node,where):

            if left > right:
                return
            
            mid = (left+right)//2

            if where == 'left':
                node.left = TreeNode(nums[mid])
                node = node.left
            else:
                node.right = TreeNode(nums[mid])
                node = node.right

            if left == right :
                return 

            add_node(left,mid-1,node,'left')
            add_node(mid+1,right,node,'right')

        left = 0
        right = len(nums)-1
        
        mid = right//2

        root = TreeNode(nums[mid])
        
        add_node(left,mid-1,root,'left')
        add_node(mid+1,right,root,'right')

        return root
