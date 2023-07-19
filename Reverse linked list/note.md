Link: https://leetcode.com/problems/reverse-linked-list/description/?envType=featured-list&envId=top-interview-questions
# Approach
Calling the function recursively and keeping track of previous, current & next node at every calls.
In the function we move forward each time & pointing the next of current node to previous node.

# Complexity
- Time complexity: $$O(n)$$ 

- Space complexity: $$O(1)$$