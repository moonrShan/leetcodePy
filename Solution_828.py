import collections


class Solution_828:
    def uniqueLetterString(self, s: str) -> int:
        c = collections.defaultdict(list)
        for i, ch in enumerate(s):
            c[ch].append(i)
        result = 0
        for pos in c.values():
            pos = [-1] + pos + [len(s)]
            for i in range(1, len(pos) - 1):
                result += (pos[i] - pos[i - 1]) * (pos[i + 1] - pos[i])
        return result


