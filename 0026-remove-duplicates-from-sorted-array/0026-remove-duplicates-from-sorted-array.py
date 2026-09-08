class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        nums1=tuple(nums)
        nums1=set(nums1)
        nums1=list(nums1)
        nums1.sort()
        b=len(nums1)
        for i in range(b):
            nums[i]=nums1[i]
        return b