class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        # Base case for k == 0
        if k == 0:
            return [0] * n
            
        ans = []
        for i in range(n):
            s = 0
            
            if k > 0:
                # Sum the next k elements
                for j in range(i + 1, i + k + 1):
                    s += code[j % n]
            else:
                # Sum the previous |k| elements
                for j in range(i + k, i):
                    s += code[j % n]
                    
            ans.append(s)
            
        return ans