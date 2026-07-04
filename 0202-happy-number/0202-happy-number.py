class Solution:
    def isHappy(self, n: int) -> bool:
        def isnum(n):
            s=0
            
            while n!=0:
                r=n%10
                s+=r*r
                n//=10
            return s
        
        slow=n
        fast=n
        while True:
            slow=isnum(slow)
            fast=isnum(isnum((fast)))
            if slow==fast:
                break
        return slow==1