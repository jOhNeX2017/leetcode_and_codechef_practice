Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/?envType=featured-list&envId=top-interview-questions
# Intuition
As we have the sorted array, so the mid of the input is gonna be root node, If we apply the same approach to every sub tree then we will get the 
height balanced tree.
# Approach
Begin by generating a root node using the middle element of the input array. Next, split the array into two parts: the left subarray (from the zero index to mid-1 index) and the right subarray (from mid+1 index to the last index). For each subtree, create a root node using the mid element from the left subarray for the left subtree and similarly for the right subtree from the right subarray. Repeat this process for every subtree. 

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$(for the new tree)