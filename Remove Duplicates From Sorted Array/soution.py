#Approach -
# In this, I have created the index variable where we will put the value
# And the result varaible to count the total number of ditinct values
# Update the result and index only when there is the change in the array value

class Solution:
    def removeDuplicates(self, nums):
        result = 1
        n = len(nums)
        index = 1
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                result+=1
                nums[index] = nums[i+1]
                index+=1
            
            
        return result