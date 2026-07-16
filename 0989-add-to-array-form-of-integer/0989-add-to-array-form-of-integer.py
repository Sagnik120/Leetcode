class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = 0

        # Convert array to integer
        for n in num:
            s = s * 10 + n

        s += k

        # Special case
        if s == 0:
            return [0]

        ans = []

        # Convert integer back to array
        while s > 0:
            ans.append(s % 10)
            s //= 10

        ans.reverse()
        return ans