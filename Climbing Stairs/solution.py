class Solution:
    def __init__(self):
        self.dic = {1:1,2:2}

    def dp(self,n):
        if self.dic.get(n):
            return self.dic[n]
        else:
            self.dic[n] = self.dp(n-1) + self.dp(n-2)
            return self.dic[n]

    def climbStairs(self, n: int) -> int:
        # dic = {1:1,2:2}
        self.dp(n)
        return self.dic[n]