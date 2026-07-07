class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for x in arr1:
            ok = True
            for y in arr2:
                if abs(x - y) <= d:
                    ok = False
                    break
            if ok:
                count += 1
        return count