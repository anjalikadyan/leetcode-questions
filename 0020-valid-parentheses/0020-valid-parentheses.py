class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        a=[]
        match = {')': '(', '}': '{', ']':'['}
        count=0
        for i in s:
            if i in match:
                if len(a)==0:
                    return False
                if len(a)>0:
                    count+=1
                    if match[i]!=a.pop():
                        return False
                    
            else:
                a.append(i)
        # if count==0:
        #     return False
        if count>0 and len(a)==0:
            return True
        return False
        
