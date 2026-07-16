class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        
        # Decrement until we find a perfect divisor
        while area % w != 0:
            w -= 1
            
        # The first divisor found yields the optimal [L, W]
        return [area // w, w]