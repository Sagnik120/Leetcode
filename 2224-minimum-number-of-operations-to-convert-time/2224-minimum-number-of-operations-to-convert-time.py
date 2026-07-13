class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ch, cm = map(int, current.split(":"))
        th, tm = map(int, correct.split(":"))

        current_minutes = ch * 60 + cm
        correct_minutes = th * 60 + tm

        diff = correct_minutes - current_minutes

        ans = 0
        for step in [60, 15, 5, 1]:
            ans += diff // step
            diff %= step

        return ans