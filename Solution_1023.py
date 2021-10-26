class Solution_1023:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        for query in queries:
            result.append(self.match(query, pattern))
        return result

    def match(self, query, pattern):
        i = 0
        for c in query:
            if i < len(pattern) and c == pattern[i]:
                i += 1
            elif ord('Z') >= ord(c) >= ord('A'):
                return False
        return i == len(pattern)