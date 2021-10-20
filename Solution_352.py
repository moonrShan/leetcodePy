class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        low, high = 0, len(self.intervals) - 1
        while low <= high:
            mid = (low + high) // 2
            elem = self.intervals[mid]
            if elem[0] <= val <= elem[1]:
                return
            elif elem[0] > val:
                high = mid - 1
            else:
                low = mid + 1

        pos = high + 1
        self.intervals[pos:pos] = [[val, val]]

        if pos + 1 < len(self.intervals) and val == self.intervals[pos + 1][0] - 1:
            self.intervals[pos][1] = self.intervals[pos + 1][1]
            self.intervals[pos + 1:pos + 2] = []

        if pos - 1 >= 0 and val == self.intervals[pos - 1][1] + 1:
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            self.intervals[pos:pos + 1] = []

    def getIntervals(self):
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()