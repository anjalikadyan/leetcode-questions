class Solution:
    def countCommas(self, n: int) -> int:
        s=1000
        c=0
        while n>=s:
            c+=(n-s+1)
            s*=1000
        return c