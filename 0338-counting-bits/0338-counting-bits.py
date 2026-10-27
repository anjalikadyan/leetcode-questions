class Solution:
    def countBits(self, n: int) -> list[int]:
        arr=[0]*(n+1)
        sub=1
        for i in range(1,n+1):
            if sub*2==i:
                sub=i
            arr[i]=arr[i-sub]+1
        return arr