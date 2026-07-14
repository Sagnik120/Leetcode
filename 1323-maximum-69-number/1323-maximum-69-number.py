class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        ans=""
        i=0
        flag=True
        while i<len(s):
            if s[i]=='6' and flag:
                ans+='9'
                flag=False
            else:
                ans+=s[i]
            i+=1
        return int(ans)