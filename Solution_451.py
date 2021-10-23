import collections


class Solution_451:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        result = ''
        for key, value in sorted(counter.items(),reverse = True, key = lambda x: x[1]):
            result += key * value
        return result