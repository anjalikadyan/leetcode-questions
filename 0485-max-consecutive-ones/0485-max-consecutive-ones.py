class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        d=0
        for i in nums:
            if i==1:
                count+=1
            if i!=1:
                count=0
            d=max(d,count)
            # print(i,count)
        return d