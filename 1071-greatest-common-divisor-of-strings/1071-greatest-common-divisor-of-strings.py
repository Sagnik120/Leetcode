class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        minStr, maxStr = (
            (str1, str2) if len(str1) < len(str2) else (str2, str1)
        )

        for i in range(len(minStr), 0, -1):
            unit = len(minStr) // i
            syllable = minStr[:i]

            if syllable * unit == minStr:
                unitMaxStr = len(maxStr) // len(syllable)
                if syllable * unitMaxStr == maxStr:
                    return syllable

        return ""