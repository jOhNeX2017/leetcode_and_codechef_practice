# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
All the number in a string to be added to find the value, only have to handle the case for 4(IV),9(IX),40(XL),90(XC)....

# Approach
<!-- Describe your approach to solving the problem. -->
Go through each alphabet in string and compare it with the next alphabet if the value of the current alphabet is lesser than the next one then subtract that alphabet value from the sum else add the number.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$ 