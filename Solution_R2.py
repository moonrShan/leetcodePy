from typing import List


class Solution_R2:
    def CountAnalogyArr(self, differences: List[int], lowBound: int, upBound: int):
        minValue = 0
        maxValue = 0
        value = 0
        for difference in differences:
            value += difference
            minValue = min(value, minValue)
            maxValue = max(value, maxValue)

        count = upBound - lowBound + 1 - (maxValue - minValue)
        return count if count > 0 else 0

def main():
    testObject = Solution_R2()
    print(testObject.CountAnalogyArr( [-2, -1, -2, 5],3,10))

if __name__=="__main__":
    main()