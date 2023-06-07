

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Inorder traversing in the binary tree is done in the following way:-

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
    def inorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        res = []

        def traversing(node):
            if node:
                traversing(node.left)
                res.append(node.val)
                traversing(node.right)
        
        traversing(node)
        return res
```

#### URL: https://leetcode.com/problems/binary-tree-inorder-traversal/description/