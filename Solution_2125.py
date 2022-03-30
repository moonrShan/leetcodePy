from typing import List


class Solution_2125:
    def numberOfBeams(self, bank: List[str]) -> int:
        deviceLine = []
        for b in bank:
            count = 0
            for c in b:
                count += c == "1"
            if count:
                deviceLine.append(count)
        result = 0
        for i in range(len(deviceLine) - 1):
            result += deviceLine[i] * deviceLine[i + 1]
        return result
