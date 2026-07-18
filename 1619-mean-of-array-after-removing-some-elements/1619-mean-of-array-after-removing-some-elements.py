class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        k = len(arr) // 20
        trimmed_arr = arr[k : len(arr) - k]
        return sum(trimmed_arr) / len(trimmed_arr)