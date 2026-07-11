class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frq=Counter(s)
        return len(set(frq.values()))==1