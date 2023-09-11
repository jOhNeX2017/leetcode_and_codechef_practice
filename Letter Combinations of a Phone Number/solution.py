## https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=featured-list&envId=top-interview-questions?envType%3Dfeatured-list&envId=top-interview-questions

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_key = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        result = []

        def parse(res,nextdigit):
            if len(nextdigit) == 0:
                result.append(res)
            else:
                for i in phone_key[nextdigit[0]]:
                    parse(res+i, nextdigit[1:])
                    
        if len(digits):
            parse('',digits)
        return result
