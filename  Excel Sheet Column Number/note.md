## Climbing Stairs

# Solution 1
## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Looking into columTitle as we the column title starts having two letters then there multiplication of 26 starts getting into pictur as we move forward to each index of columnTitle

## Approach
<!-- Describe your approach to solving the problem. -->
A simple math's as we go on increasing the index we have to multiply that letter value with 26 and also incresing the 26 power each time as the index increases.
Fourmula : value of letter * (26^index) [indexing start from right to left]

## Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->