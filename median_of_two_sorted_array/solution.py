# Approach
# Using mergesort merge method to merge two sorted array


class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        combine = []
        n,m = len(nums1),len(nums2)
        i=0
        j=0
        while(i<n and j<m):
            if nums1[i]<nums2[j]:
                combine.append(nums1[i])
                i+=1
            else:
                combine.append(nums2[j])
                j+=1
        while(i<n):
            combine.append(nums1[i])
            i+=1
        while(j<m):
            combine.append(nums2[j])
            j+=1
        median =0
        if (n+m)%2 == 0:
            idx = (n+m)//2
            median = (combine[idx]+combine[idx-1])/2
        else:
            idx = (n+m)//2
            median = combine[idx]
        
        return median