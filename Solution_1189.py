import collections


class Solution_1189:
    def maxNumberOfBalloons(self, text: str) -> int:
        usefulCharSet = {'b','a','l','o','n'}
        count = collections.defaultdict(int)
        for char in text:
            if char in usefulCharSet:
                if char == 'l' or char == 'o':
                    count[char] += 0.5
                else:
                    count[char] += 1
        return int(min(count.values())) if len(count) == 5 else 0