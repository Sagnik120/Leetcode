class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        ans=[]
        flag=1
        for i in range(len(digits)-1,-1,-1):
            sum1=digits[i]+flag+carry
            flag=0
            carry=sum1//10
            ans.append(sum1%10)
        if carry==1:
            ans.append(1)
        ans.reverse()
        return ans      