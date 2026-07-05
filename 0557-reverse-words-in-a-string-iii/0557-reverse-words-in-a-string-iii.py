class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        start = 0
        while start < n:
            end = start
            # Find the end of the current word
            while end < n and s[end] != ' ':
                end += 1
            # Reverse the word
            left, right = start, end - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            # Move to the next word
            start = end + 1
        return "".join(s)

