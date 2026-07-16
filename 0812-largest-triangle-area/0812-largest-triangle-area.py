from itertools import combinations
from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0
        
        # Check every combination of 3 distinct points
        for p1, p2, p3 in combinations(points, 3):
            # Shoelace Formula for area of a triangle
            # Area = 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
            area = 0.5 * abs(
                p1[0] * (p2[1] - p3[1]) + 
                p2[0] * (p3[1] - p1[1]) + 
                p3[0] * (p1[1] - p2[1])
            )
            if area > max_area:
                max_area = area
                
        return max_area