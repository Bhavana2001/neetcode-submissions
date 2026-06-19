from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through nums and 
        # create an hashmap w/ key = element,
        # and val = index of element

        # loop through nums, 
        # check if target - this element exists in hashmap
        # if so return index(val) associated w/ element(key)

        #dictionary = {val: i for i, val in enumerate(nums) }
        dictionary = {}
        i = 0
        for num in nums:           
            if target-num in dictionary:
                return [dictionary[target - num], i]
            dictionary[num]= i
            i += 1
        