class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        
        neg=num<0
        num=abs(num)

        ans=[]
        
        while num:
            ans.append(str(num%7))
            num//=7
        if neg:
            ans.append("-")

        return "".join(ans[::-1])