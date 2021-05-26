#Approach
# This approach is using O(n3) time complexity 
# Here we use two pointer algorithm and we taken two pointer before in which one is looped from 0 to n-1
# And second one is looping from the i to n-1
# And for the rest of element we used two pinters
from functools import cmp_to_key

class Solution:         #Approach 1
    def fourSum(self, arr,  target):
        n = len(arr)
        if n < 4:
            return []
        arr.sort()
        result =set()
        
        for i in range(n):
            # while(i+1<n and arr[i]==arr[i+1]) :
            #         i+=1
            for j in range(i+1,n):
                # while(j+1<n and arr[j]==arr[j+1]) :
                #     j+=1
                p = j+1
                q = n-1
                while(p<q):
                    if arr[i] + arr[j] + arr[p] + arr[q] == target:
                        result.add((arr[i],arr[j],arr[p],arr[q]))
                        while(p<q and arr[p] == arr[p+1]):              #to increment the p to next distinct value
                            p+=1
                        while(p<q and arr[q] == arr[q-1]):              #to increment the q to next distinct value
                            q-=1
                        p+=1
                        q-=1
                    elif arr[i] + arr[j] + arr[p] + arr[q] < target:
                        p+=1
                    else:
                        q-=1
                
            
        
        return result





if __name__ == '__main__':
    arr = [1,0,-1,0,-2,2]
    n = len(arr)
    a = Solution()
    print(a.fourSum(arr,0))
    


