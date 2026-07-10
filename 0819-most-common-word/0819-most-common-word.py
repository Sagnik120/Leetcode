class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Replace punctuation with spaces
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.lower().split()

        banned = set(banned)

        freq = Counter()

        for word in words:
            if word not in banned:
                freq[word] += 1

        return max(freq, key=freq.get)

        