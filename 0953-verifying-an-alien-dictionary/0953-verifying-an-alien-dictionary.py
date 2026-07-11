class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Store the rank of each character
        rank = {}
        for i, ch in enumerate(order):
            rank[ch] = i

        # Compare every adjacent pair of words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            j = 0

            # Compare characters one by one
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
                j += 1

            # If all compared characters are equal,
            # the shorter word should come first.
            else:
                if len(w1) > len(w2):
                    return False

        return True