import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = np.ones(len(nums))
        suffix = np.ones(len(nums))
        prefix[0] = nums[0]
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        print("prefix: ", prefix)
        print("suffix: ", suffix)
        output = np.zeros(len(nums))
        output[0] = suffix[1]
        output[len(nums)-1] = prefix[len(nums)-2]
        for i in range(1, len(nums) - 1):
            output[i] = prefix[i-1] * suffix[i+1]
        return output.astype(int).tolist()