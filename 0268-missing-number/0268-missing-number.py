class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums=sorted(nums)
        print(nums)
        n=len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i
        return -1