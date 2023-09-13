class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findInIndex(pos):
            l = pos[0]
            r = pos[1]

            if l>r:
                return -1

            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if l == r and r == mid:
                return -1

            if nums[mid] > target:
                return findInIndex([l,mid-1])
            else:
                return findInIndex([mid+1,r])

        k=-1
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                k = i
                break
        
        if k==-1:
            return findInIndex([0,n-1])
        
        k=k+1

        m = k + n//2
        if m >= n:
            m = abs(n-m)

        if target == nums[m]:
            return m

        left_part = [k,m-1 if m-1>0 else n-1]
        right_part = [m+1 if m+1 < n else 0,k-1]

        if  nums[m] > target:   
            # For LEFT PART
            if left_part[0] > left_part[1]:
                left_sub1 = [left_part[0], n-1]
                left_sub2 = [0,left_part[1]]
                return findInIndex(left_sub1) & findInIndex(left_sub2) 

            else:
                return findInIndex(left_part)
        else:
            # For RIGHT PART
            if right_part[0] > right_part[1]:
                right_sub1 = [right_part[0],n-1]
                right_sub2 = [0,right_part[1]]
                return findInIndex(right_sub1) & findInIndex(right_sub2) 

            else:
                return findInIndex(right_part)
        
            
