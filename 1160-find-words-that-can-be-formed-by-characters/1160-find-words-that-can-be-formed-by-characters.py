class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}

        for ch in chars:
            freq[ch] = freq.get(ch, 0) + 1

        ans = 0

        for word in words:
            temp = {}

            for ch in word:
                temp[ch] = temp.get(ch, 0) + 1

            ok = True

            for ch in temp:
                if temp[ch] > freq.get(ch, 0):
                    ok = False
                    break

            if ok:
                ans += len(word)

        return ans