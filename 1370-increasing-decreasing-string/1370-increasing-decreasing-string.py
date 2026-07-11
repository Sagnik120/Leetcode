class Solution:
    def sortString(self, s: str) -> str:
        freq = Counter(s)
        ans = []

        while len(ans) < len(s):

            # Increasing order
            for ch in sorted(freq.keys()):
                if freq[ch] > 0:
                    ans.append(ch)
                    freq[ch] -= 1

            # Decreasing order
            for ch in sorted(freq.keys(), reverse=True):
                if freq[ch] > 0:
                    ans.append(ch)
                    freq[ch] -= 1

        return "".join(ans)