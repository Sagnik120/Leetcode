class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        count = 0

        for ch in reversed(s):
            if ch == "-":
                continue

            if count == k:
                ans.append("-")
                count = 0

            ans.append(ch.upper())
            count += 1

        return "".join(reversed(ans))