def romanToInt(self, s: str) -> int:
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    number=0
    n = len(s)
    for i in range(0,n-1):
        if roman[s[i]] < roman[s[i+1]]:
            number -= roman[s[i]]
        else:
            number += roman[s[i]]
    
    number += roman[s[n-1]]

    return number