class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1

            if freq[ch]==2:
                return ch