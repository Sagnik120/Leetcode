class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frq = {}

        # Count characters in magazine
        for ch in magazine:
            frq[ch] = frq.get(ch, 0) + 1

        # Use characters for ransomNote
        for ch in ransomNote:
            frq[ch] = frq.get(ch, 0) - 1

            if frq[ch] < 0:
                return False

        return True