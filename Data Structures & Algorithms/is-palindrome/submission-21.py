class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s))
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].upper() != s[end].upper():
                return False
            start = start + 1
            end = end - 1

        return True
        