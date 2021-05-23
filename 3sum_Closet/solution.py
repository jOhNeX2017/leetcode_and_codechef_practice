#Approach:
# Used two pointer algorithms and minimum diffrence b/w the target and current sum.
# We first sort the array and after that we set the minimum diffrence intially to max 
# fixed one pointer to end of the array and move it towards the array starting 
# now for the rest of the array apply the two pointer algorithm so that we can calulate three values sum.
# After this check the diffrence b/w the target and sum value, and update the minumu diffrence accordingly
# return the diffrence b/w target and minimum diffrence


class Solution:
    def threeSumClosest(self, arr, target):
        # res = set()
        arr.sort()
        n =len(arr)
        minimum_diff = 10001
        for k in range(n-1,1,-1):
            i=0
            j=k-1
            while(i<j):
                temp = arr[k]+arr[i]+arr[j] 
                if temp == target:
                    return temp
                elif temp > target:
                    j-=1
                else:
                    i+=1
                if abs(target-temp) < abs(minimum_diff):
                    minimum_diff = target - temp
        return target - minimum_diff
                    