class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        state = [0] * 101

        for bulb in bulbs:
            state[bulb] ^= 1

        ans = []

        for i in range(1, 101):
            if state[i]:
                ans.append(i)

        return ans