#Approach:
# Using two pointer algorithm
# Move i if height at i is less than height at j else move j

class Solution:
    def maxArea(self, height):
        i,j = 0,len(height)-1
        maxarea = 0
        while(i<j):
            b = j-i
            h = height[j] if height[j]<height[i] else height[i]
            if b*h > maxarea :
                maxarea = b*h
            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        return maxarea