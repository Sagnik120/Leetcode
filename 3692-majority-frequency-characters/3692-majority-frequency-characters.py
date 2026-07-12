class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)
        groups = defaultdict(list)

        for ch, f in freq.items():
            groups[f].append(ch)

        ans = []
        max_size = 0
        max_freq = -1

        for f, chars in groups.items():
            if len(chars) > max_size or (len(chars) == max_size and f > max_freq):
                max_size = len(chars)
                max_freq = f
                ans = chars

        return "".join(ans)