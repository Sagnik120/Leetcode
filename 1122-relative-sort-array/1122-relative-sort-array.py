class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        ans = []
        # Add elements in the order of arr2
        for num in arr2:
            ans.extend([num] * freq[num])
            del freq[num]
        # Add remaining elements in sorted order
        for num in sorted(freq.keys()):
            ans.extend([num] * freq[num])

        return ans