class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_pairs = {'{':'}', '(':')', '[':']' }
        for char in s:
            if (char == '{' or char == '[' or char == '('):
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False
                pair = stack.pop()

                if char != paren_pairs.get(pair):
                    return False

        return len(stack) == 0
        

