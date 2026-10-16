class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=nums
        nums=set(nums)
        if len(n)!=len(nums):
            return True
        return False