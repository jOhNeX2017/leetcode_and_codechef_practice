## Link: https://leetcode.com/problems/valid-anagram/description/?envType=featured-list&envId=top-interview-questions
def isAnagram(s: str, t: str):
    dicA = {}
    dicB = {}

    for letter in s:
        if not dicA.get(letter):
            dicA[letter] = 1
        else:
            dicA[letter] +=1
    
    for letter in t:
        if not dicB.get(letter):
            dicB[letter] = 1
        else:
            dicB[letter] +=1
    
    return dicA == dicB