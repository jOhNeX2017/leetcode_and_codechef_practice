class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = nums1+nums2
        list1.sort()
        n = len(list1)
        if n%2==0:
            num = (list1[n//2]+list1[(n//2)-1])/2
            return num
        else:
            n = (n-1)//2
            return list1[n]
