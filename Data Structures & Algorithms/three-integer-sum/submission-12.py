class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i,a in enumerate(nums):
            if(i > 0 and a == nums[i-1]):
                continue
            
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                if (a + nums[start] + nums[end] > 0):
                    end -= 1
                    
                elif (a + nums[start] + nums[end] < 0):
                    start += 1
                    
                else:
                    result.append([a, nums[start], nums[end]])
                    start += 1
                    while(nums[start] == nums[start -1] and start < end):
                        start += 1
                        end -=1
        return result
        """start = 0
        start2 = start + 1 
        end = len(nums) - 1
        prev = None
        prev2 = None
        prev_end = None

        while (start < end):
            if(prev != None and nums[start] == nums[prev]):
                start += 1
                continue
            while(start2 < end):
                if (nums[start] + nums[start2] + nums[end] == 0):
                    #if ([nums[start], nums[start2], nums[end]] not in result):
                    result.append([nums[start], nums[start2], nums[end]])
                    start2 += 1
                    while(nums[start2] == nums[start2 - 1] and start2 < end):
                        start2 += start2

                if (nums[start] + nums[start2] + nums[end] < 0):
                    prev2 = start2
                    start2 += 1
                    continue
                if (nums[start] + nums[start2] + nums[end] > 0):
                    prev_end = end
                    end -= 1
                    continue
            prev = start
            start += 1
            start2 = start + 1
        return result"""
        
       



        