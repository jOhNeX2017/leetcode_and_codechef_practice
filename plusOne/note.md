## Link: https://leetcode.com/problems/plus-one/description/

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
First : To convert the list into an intger then add 1 to it and again convert back it to list

Second: Read the integer from the last and whenever the intger is equal to 9, then only I will traverse futher else will break the loop and add the 1 to the current integer

# Approach
<!-- Describe your approach to solving the problem. -->
While traversing, whenever the current value is 9, we make that value zero and continue traversing. While traversing, if we find any value less than 9, we add 1 to it and stop traversing. If we don't find any value less than 9, we continue traversing. When we reach the end of the array, we append 0 and make the first value 1 only if the first value is equal to 9.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity:$$O(0)$$

# Code
```
class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        n = len(arr) -1

        while n >=1:
            if arr[n]<9:
                arr[n]+=1
                break
            else:
                arr[n]=0
            n-=1

        if n==0:
            if arr[0] < 9:
                arr[0]+=1
            else:
                arr.append(0)
                arr[0] = 1

        return arr
    
```