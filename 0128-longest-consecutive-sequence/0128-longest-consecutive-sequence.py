class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)
        counter = 1
        ans = 0
        for i in range(0, len(nums)):
            num = nums[i]
            if num not in nums_set:
                continue
            nums_set.remove(num)
            val = num

            while(True):
                val -= 1
                if val in nums_set:
                    nums_set.remove(val)
                    counter += 1
                else:
                    break
            
            val = num
            while(True):
                val += 1
                if val in nums_set:
                    nums_set.remove(val)
                    counter += 1
                else:
                    break
            
            ans = max(ans, counter)
            counter = 1
        
        # ans = max(ans, counter)
        return ans
        