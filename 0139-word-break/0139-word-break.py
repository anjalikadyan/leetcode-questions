class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word=set(wordDict)
        n=len(s)
        d=[False]*(n+1)
        d[0]=True
        for i in range(1,n+1):
            for j in range(i):
                if d[j] and s[j:i] in word:
                    d[i]=True
                    break
        return d[n]
            
            