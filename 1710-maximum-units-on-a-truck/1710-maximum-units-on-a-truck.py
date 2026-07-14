class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0

        for boxes, units in boxTypes:
            # Take as many boxes as possible
            take = min(boxes, truckSize)

            total_units += take * units
            truckSize -= take

            if truckSize == 0:
                break

        return total_units