class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(target)

        ans = float('inf')

        for ch in cnt_t:
            ans = min(ans, cnt_s[ch] // cnt_t[ch])

        return ans