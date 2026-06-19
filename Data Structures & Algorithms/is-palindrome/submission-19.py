class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = s.upper()
        #s = "".join(filter(str.isalnum, s))
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start+= 1
                continue
            if not (s[end].isalnum()):
                end -= 1
                continue
            if s[start].upper() != s[end].upper():
                return False
            start += 1
            end -= 1

        return True
        