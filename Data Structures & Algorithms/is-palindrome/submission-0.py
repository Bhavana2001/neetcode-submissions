class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.upper()
        s = "".join(filter(str.isalnum, s))
        start = 0
        end = len(s) - 1
        print(s)
        for i in range(int(len(s)/2)):
            if s[start] != s[end]:
                return False
            start = start + 1
            end = end - 1

        return True
        