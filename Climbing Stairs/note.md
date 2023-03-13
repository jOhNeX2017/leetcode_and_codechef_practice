## https://leetcode.com/problems/climbing-stairs/

# Solution 1
## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
As we can have only two moves possible i.e either move 1 step or move 2 step at a time. So, I start decreasing the steps by 1 or 2 everytime.
So that, as I reach to 1 or 2 steps only, I always have a count for them and we are just going to add them to the values.

## Approach
<!-- Describe your approach to solving the problem. -->
I use DP where I am storing the result on dictionary, So that I dont have to calculate the same values again.

## Complexity
- Time complexity: $$O(nlog(n))$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Solution 2 - Fibonacii series way
## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
On analysis of the results of diffrent numbers I found that this is creating the $ fibonacii-series $. For example,
1-1,2-2,3-3,4-5,5-8,6-13,7-21,..........
If we take the soutions only it forms a series 1,2,3,5,8,13,21,.......
which is $fibonacii$.

## Approach
<!-- Describe your approach to solving the problem. -->
Adding the a & b each time and replacing the older values with the new added values in the way a,b becomes b, a+b respectively.
 
## Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->