class Solution:
    def isHappy(self, n: int) -> bool:

        def get_happy(n):
            temp = 0
            while n >0:
                last_digit = n%10
                temp += last_digit*last_digit
                n = n//10
            return temp
        
        while n>9:
            n = get_happy(n)

        if n in [1,7]:
            return True
        else:
            return False