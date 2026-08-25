class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        a=k
        while a in s:
            a+=k
        return a