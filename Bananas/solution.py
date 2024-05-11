def bananas(s):
    # Your code here!
    res = set()
    rec(s,res)
    return res

def rec(word, result, cur_word='banana', res='' ):    
    if len(cur_word) == 0: #banana is formed
        
        if len(word) > 0:  #banana is formed but still few letters left at the end of the string
            temp='-'
            temp*=len(word)
            result.add(res+temp)  #adding the value to result
        else:
            result.add(res)  #adding the value to result
        
    if len(cur_word)> 0 and len(word)>0: 
        
        if len(word) >= len(cur_word):
        
            rec(word[1:], result, cur_word, res+'-')  #Passing all the possibilties

            if cur_word[0] == word[0]:
                rec(word[1:],result, cur_word[1:], res+word[0]) #when letter matched 