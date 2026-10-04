class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=0:
            return 0
        if len(s)==1:
            return 1


        l=0
        d=0
        for i,x in enumerate(s):
            s1={}
            l=0
            for j in range(i,len(s)):
                if s[j] in s1:
                    break
                l+=1
                s1[s[j]]=j
            d=max(d,l)
        return d




        