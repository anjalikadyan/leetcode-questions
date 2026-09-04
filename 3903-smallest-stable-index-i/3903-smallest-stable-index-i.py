class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            maxi=nums[i]
            mini=nums[i]
            for j in range(0,i):
                if nums[j]>maxi:
                    maxi=nums[j]
            for j in range(i,len(nums)):
                if nums[j]<mini:
                    mini=nums[j]
            add=maxi-mini
            if add<=k:
                return i
        return -1