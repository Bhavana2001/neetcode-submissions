from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
 
        start = 0
        end = start + len(s1)
        while end < len(s2) + 1:
            if (Counter(s1) == Counter(s2[start:end])):
                return True
            else:
                start += 1
                end += 1
        return False
        