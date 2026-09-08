class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        num=set(nums)
        arr=[]
        for i in range(1,n+1):
            if i not in num:
                arr.append(i)
        return arr
