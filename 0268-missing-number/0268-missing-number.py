class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        if nums[n-1]!=n:
            return n
        for i in range(0,n):
            if nums[i]!=i:
                return i
        return -1