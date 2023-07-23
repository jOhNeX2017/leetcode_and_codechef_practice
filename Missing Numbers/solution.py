## Link : https://leetcode.com/problems/missing-number/description/?envType=featured-list&envId=top-interview-questions
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        addition_of_val = sum(nums)
        n=len(nums)
        actual_value = (n*(n+1))//2
        
        if actual_value == addition_of_val:
            return 0


        return actual_value-addition_of_val