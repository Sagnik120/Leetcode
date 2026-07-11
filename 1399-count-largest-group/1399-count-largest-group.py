class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}

        for num in range(1, n + 1):
            digit_sum = 0
            temp = num

            while temp:
                digit_sum += temp % 10
                temp //= 10

            freq[digit_sum] = freq.get(digit_sum, 0) + 1

        largest = max(freq.values())

        ans = 0

        for count in freq.values():
            if count == largest:
                ans += 1

        return ans