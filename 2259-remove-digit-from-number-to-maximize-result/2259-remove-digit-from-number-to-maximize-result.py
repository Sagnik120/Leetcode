class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s=list(number)
        ans=""
        for i in range(len(number)):
            if number[i] == digit:
                curr = number[:i] + number[i + 1:]
                if curr > ans:
                    ans = curr

        return ans