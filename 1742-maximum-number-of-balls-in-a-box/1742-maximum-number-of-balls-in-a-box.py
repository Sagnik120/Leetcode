class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = {}
        ans = 0

        for num in range(lowLimit, highLimit + 1):
            digit_sum = 0
            temp = num

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            box[digit_sum] = box.get(digit_sum, 0) + 1
            ans = max(ans, box[digit_sum])

        return ans