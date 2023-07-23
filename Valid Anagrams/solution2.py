## Link: https://leetcode.com/problems/valid-anagram/description/?envType=featured-list&envId=top-interview-questions
def isAnagram(self, s: str, t: str) -> bool:s
    alpha = 'qwertyuiopasdfghjklzxcvbnm'

    for letter in alpha:
        if s.count(letter) != t.count(letter):
            return False
    return True