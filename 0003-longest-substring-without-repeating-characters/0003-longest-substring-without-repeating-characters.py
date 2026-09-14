class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start=length=0
        c={}
        for i,x in enumerate(s):
            if x in c and start<=c[x]:
                start=c[x]+1
            else:
                length=max(length,i-start+1)
            c[x]=i
        print(c)
        return length


        