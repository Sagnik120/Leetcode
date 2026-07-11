class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()

        freq = Counter(words)

        ans = []

        for word, count in freq.items():
            if count == 1:
                ans.append(word)

        return ans