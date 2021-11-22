class Solution_2075:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        rowList = []
        rowLength = len(encodedText) // rows
        for i in range(rows):
            rowList.append(encodedText[i*rowLength:i*rowLength+rowLength])
        i = 0; j = 0; k = 0
        result = ''
        while i < rows and j < rowLength:
            result += rowList[i][j]
            i += 1
            j += 1
            if i == rows:
                i = 0
                j = k + 1
                k += 1
        return result.rstrip()