class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)-1
        i=0
        d=0
        while i<=n:
            l=height[i]
            r=height[n]
            w=n-i
            sum=0
            h=min(l,r)
            sum=h*w
            if l<r:
                i+=1
            else:
                n-=1
            d=max(d,sum)
        return d




        
        

        