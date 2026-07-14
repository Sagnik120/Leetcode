class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        ans = 0

        for ch in word:
            d = abs(ord(ch) - ord(curr))
            ans += min(d, 26 - d) + 1
            curr = ch

        return ans