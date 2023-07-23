## Link: https://leetcode.com/problems/palindrome-linked-list/description/?envType=featured-list&envId=top-interview-questions
# Intuition
To check for a palindrome in a linked list, typically two methods are commonly used:

    1. Compare the original string with its reverse string.
    2. Compare values from both ends, starting from the middle and moving towards the ends.
    
By modifying the second method slightly, we can come up with another approach. We can use two pointers, starting from the middle, and compare each letter as we move towards the ends.

To do this, first, we use a fast pointer to find the middle of the linked list. When the fast pointer reaches the end of the linked list, the slow pointer will be at the mid of the linked list.


# Complexity
- Time complexity: $$O(n)$$

- Space complexity:  $$O(1)$$
