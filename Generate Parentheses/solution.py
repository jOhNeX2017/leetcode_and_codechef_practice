class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(val,n,stack):
            if n == 0:
                if len(stack) == 0:
                    result.append(val)
                return
            
            curr_stack = stack.copy()
            curr_stack.append('(')
            recursive(val+'(',n-1,curr_stack)

            curr_stack = stack.copy()
            if len(curr_stack)>0 :
                m = len(curr_stack)-1
                if curr_stack[m] == '(':
                    
                    del curr_stack[m]
                    recursive(val+')',n-1,curr_stack)
                else:
                    curr_stack.append(')')
                    recursive(val+')',n-1,curr_stack)
            else:
                curr_stack.append(')')
                recursive(val+')',n-1,curr_stack)

        result = []
        recursive('(',(n*2)-1,['('])
        return result