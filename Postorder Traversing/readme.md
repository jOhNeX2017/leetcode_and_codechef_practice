

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
postorder traversing in the binary tree is done in the following way:-

left node - node - right node

in the same way I am calling the function for left part, then appending its node value to result and then calling it for right part


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        res = []

        def traversing(node):
            if node:
                traversing(node.left)
                traversing(node.right)
                res.append(node.val)
        
        traversing(node)
        return res
```

