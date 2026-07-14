class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)

        capacity.sort(reverse=True)

        boxes = 0
        curr = 0

        for cap in capacity:
            curr += cap
            boxes += 1

            if curr >= total:
                return boxes