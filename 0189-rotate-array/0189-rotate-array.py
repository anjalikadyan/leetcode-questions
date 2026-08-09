class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr=nums.copy()
        n=len(arr)
        c=k
        while(k>n):
            c=k-n
            k=c

        for i in range(n):
            if((i+c)>n-1):
                d=(i+c)-n
                nums[d]=arr[i]
            else:
                nums[i+c]=arr[i]
                
        



        