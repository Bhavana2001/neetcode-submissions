from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # checking if they both have the same number of each letter
        #loop thorough s and add each letter to a hashmap/dictionary
        # with key = letter, val = occurences
        # repeat loop with t

        # Counter from collections creates dictionary-like 
        # object w/ key = letter and val = occurences
        # dictionary-like b/c if you try to access an element
        # that DNE, will return 0 instead of 'KeyError'

        return Counter(s) == Counter(t)

        