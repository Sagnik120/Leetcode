class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = {}

        # Count required letters
        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] = need.get(ch, 0) + 1

        ans = ""

        for word in words:
            freq = {}

            # Count letters in current word
            for ch in word:
                freq[ch] = freq.get(ch, 0) + 1

            ok = True

            # Check if all required letters are present
            for ch in need:
                if freq.get(ch, 0) < need[ch]:
                    ok = False
                    break

            if ok:
                if ans == "" or len(word) < len(ans):
                    ans = word

        return ans