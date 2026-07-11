class Solution:
    def residuePrefixes(self, s: str) -> int:
        st = set()
        ans = 0
        for i, ch in enumerate(s, 1):
            st.add(ch)
            if len(st) == i % 3:
                ans += 1
        return ans