class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        sum_all = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if sum_all < desiredTotal:
            return False
        
        if desiredTotal <= 0:
            return True
        
        memo = {}
        
        def dfs(mask: int, current_total: int) -> bool:
            if mask in memo:
                return memo[mask]
            
            for i in range(1, maxChoosableInteger + 1):
                if not (mask & (1 << i)):
                    if current_total <= i:
                        memo[mask] = True
                        return True
                    
                    if not dfs(mask | (1 << i), current_total - i):
                        memo[mask] = True
                        return True
            
            memo[mask] = False
            return False
        
        return dfs(0, desiredTotal)