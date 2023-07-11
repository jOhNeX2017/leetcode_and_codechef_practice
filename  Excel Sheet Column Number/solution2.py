class Solution:
    def titleToNumber(self, columnTitle: str) -> int:        
        sum = 0
        mult = 1

        n = len(columnTitle)
        for i in range(n-1,-1,-1):
            sum += mult*(ord(columnTitle[i])-64)
            mult *=26
        return sum
            