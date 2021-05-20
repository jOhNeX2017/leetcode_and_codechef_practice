# #Approach:
# Fixing one of the pointer let say fix the k such that we decrement the value every time.
# and after that apply two pointer for the rest of the array
        # Time Complexity: O(n2) in wors case

class Solution:
    def threeSum(self, nums):
        n= len(nums)
        res=[]
        if n < 3:
            return res
        nums.sort()
        
        for k in range(n-1,1,-1):
            i,j=0,k-1
            while(i<j):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append((nums[i],nums[j],nums[k]))
                    i+=1
                    j-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j-=1
                else:
                    i+=1
        return set(res)