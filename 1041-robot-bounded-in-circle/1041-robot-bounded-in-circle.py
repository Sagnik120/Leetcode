class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        direction = 0  # North

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for ch in instructions:
            if ch == 'G':
                x += dx[direction]
                y += dy[direction]
            elif ch == 'L':
                direction = (direction + 3) % 4
            else:  # 'R'
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0
        