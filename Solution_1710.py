class Solution_1710:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        total = 0
        while truckSize and boxTypes:
            count, capacity = boxTypes.pop()
            if truckSize > count:
                total += count * capacity
                truckSize -= count
            else:
                total += truckSize * capacity
                truckSize = 0
        return total

