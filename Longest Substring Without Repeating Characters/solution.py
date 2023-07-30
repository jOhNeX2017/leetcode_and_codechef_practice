class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s):

            start_i=0
            start_j= len(set(list(s)))
            n = len(s)

            if start_j == 1:
                return 1

            if start_j == n:
                return n
            
            longest_substring = None

            while not longest_substring:
                i = start_i
                j = start_j
                while (j<=n):
                    curr_str = s[i:j]
                    if len(curr_str) == len(set(list(curr_str))):
                        longest_substring = curr_str
                        break
                    i+=1
                    j+=1
                start_j -=1
            return len(longest_substring)

            
        
        return len(s)