class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_pairs = {'}':'{', ')':'(', ']':'['}
        #paren_pairs = {'{':'}', '(':')', '[':']' }
        for char in s:
            if char in paren_pairs:
                if not stack or paren_pairs[char]!= stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
        '''
        for char in s:
            if (char == '{' or char == '[' or char == '('):
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False
                pair = stack.pop()

                if char != paren_pairs.get(pair):
                    return False

        return len(stack) == 0'''
        

