class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap w/ key = unique elements and val = count
        # loop through nums + and each element into map or increment count 
        # make array where index = frequency and element = array of numbers 
        # that appear with that frequency in nums array
        # bucket sort counts array
        # create results array which grabs k numbers at highest indices
        maps = {}
        result = []
        for index, element in enumerate(nums):
            if element in maps:
                maps[element] = maps[element] + 1
            else:
                maps[element] = 1
        counts = [None] * (len(nums) + 1)
        print("length of counts: ", len(counts))
        for key in maps:
            val = maps[key]
            print("val: ", val)
            if counts[val] != None:
                counts[val].append(key)
            else :
                counts[val] = [key]

        result = []
        for vals in reversed(counts):
            if vals != None:
                for j in vals:
                    result.append(j)
                    if (len(result) >= k):
                        return result


            



        