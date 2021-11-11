class Solution:
    def findPosLength(self,array):
        lastX = -1
        lastSpace = -1
        resultLen = float('-inf')
        resultPos = -1
        for i, s in enumerate(array):
            if s == "X":
                lastX = i
            if s == "":
                if lastX > 0 and lastSpace < lastX:
                    if i - lastX + 1 > resultLen:
                        resultLen = i - lastX + 1
                        resultPos = i
                lastSpace = i

        return (resultLen, resultPos)



#["O","O","","X","O",""]
#["X","","O","O","","X","O",""]
def main():
    testObject = Solution()
    print(testObject.findPosLength(["O","O","","X","O",""]))
    print(testObject.findPosLength(["X","","O","O","","X","O",""]))

if __name__ == "__main__":
    main()