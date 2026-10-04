class Solution:
    def countSubstrings(self, s: str) -> int:
        a=[]
        for i in range(len(s)):
            a.append(s[i])
            sub=s[i]
            for j in range(i+1,len(s)):
                sub+=s[j]
                rev=sub[::-1]
                if sub == rev:
                    a.append(sub)
        return len(a)
