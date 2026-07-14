class Solution:
    def minimumSum(self, num: int) -> int:
        num1 = list(str(num))
        num1.sort()

        ans1 = num1[0] + num1[2]
        ans2 = num1[1] + num1[3]

        return int(ans1) + int(ans2)