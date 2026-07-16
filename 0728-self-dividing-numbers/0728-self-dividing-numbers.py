class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        
        for i in range(left, right + 1):
            is_self_dividing = True
            temp = i
            
            while temp > 0:
                digit = temp % 10
                if digit == 0 or i % digit != 0:
                    is_self_dividing = False
                    break
                temp //= 10  # Move to the next digit
                
            if is_self_dividing:
                ans.append(i)
                
        return ans