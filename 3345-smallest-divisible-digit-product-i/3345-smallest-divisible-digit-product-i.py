class Solution:
    def product(self,n:int)->int:
        sum=1
        i=n
        while(i>0):
            if i<10:
                sum*=i
                break
            d=i%10
            i//=10
            sum*=d
        return sum
    def smallestNumber(self, n: int, t: int) -> int:
        i=n
        while(True):
            sum=self.product(i)
            
            if sum%t==0:
                return i
            i+=1

        