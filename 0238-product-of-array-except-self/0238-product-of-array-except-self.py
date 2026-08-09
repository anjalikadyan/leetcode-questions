class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[1]*n
        sum1=1
        for i in range(n):
            arr[i]=sum1
            sum1*=nums[i]
        sum2=1
        for i in range(n-1,-1,-1):
            arr[i]*=sum2
            sum2*=nums[i]
        return arr
