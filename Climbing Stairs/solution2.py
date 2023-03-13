def climbStairs(self, n: int) -> int:
        if n <=1:
            return 1
        else:
            a = 1
            b = 2
            for i in range(2,n):
                #t=b
                #b=a+b
                #a=t
                a,b = b,a+b

            return b