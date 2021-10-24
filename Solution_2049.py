
class Solution_2049:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = [[] for _ in parents]
        for i, x in enumerate(parents):
            if x >= 0: tree[x].append(i)

        freq = defaultdict(int)

        def fn(x):
            left = right = 0
            if tree[x]: left = fn(tree[x][0])
            if len(tree[x]) > 1: right = fn(tree[x][1])
            score = (left or 1) * (right or 1) * (len(parents) - 1 - left - right or 1)
            freq[score] += 1
            return 1 + left + right

        fn(0)
        return freq[max(freq)]
