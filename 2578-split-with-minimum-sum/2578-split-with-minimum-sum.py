class Solution:
    def splitNum(self, num: int) -> int:
        s=list(str(num))
        num1=""
        num2=""
        s.sort()
        i=0
        j=1
        for i in range(len(s)):
            if i % 2 == 0:
                num1 += s[i]
            else:
                num2 += s[i]
        return int(num1)+int(num2)
