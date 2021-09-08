from typing import List


class Solution_937:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.get_key)

    def get_key(self, log):
        _id, rest = log.split(" ", maxsplit=1)
        return (0, rest, _id) if rest[0].isalpha() else (1, 1, 1)