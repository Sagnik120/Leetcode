class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = sorted(s)

        prev_count = 0
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                if prev_count == 0:
                    prev_count = count
                elif prev_count != count:
                    return False
                count = 1

        # Check the last character group
        if prev_count == 0:
            return True
        return prev_count == count
            
