class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i ,x in enumerate(nums):
            n=target-x
            if n in s:
                return [s[n],i]
            s[x]=i