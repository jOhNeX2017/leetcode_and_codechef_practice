class Solution:
    def titleToNumber(self, columnTitle: str) -> int:        
        sum = 0

        n = len(columnTitle)
        for i in range(n):
            sum += (26**(n-i-1))*(ord(columnTitle[i])-64)

        return sum