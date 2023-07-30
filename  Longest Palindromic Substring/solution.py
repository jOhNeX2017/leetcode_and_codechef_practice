class Solution:
    def longestPalindrome(self, s: str) -> str:
            start_i=0
            n = len(s)
            start_j=  n
            
            longest_substring = None

            while not longest_substring:
                i = start_i
                j = start_j
                while (j<=n):
                    curr_str = s[i:j]
                    if curr_str == curr_str[::-1]:
                        longest_substring = curr_str
                        break
                    i+=1
                    j+=1
                start_j -=1
            
            return longest_substring