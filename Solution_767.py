class Solution_767:
    def reorganizeString(self, s: str) -> str:
        res = ""
        c = collections.Counter(s)
        heap = [(-value,key) for key, value in c.items()]
        heapq.heapify(heap)
        prefreq, prevChar = 0,''
        while heap:
            freq, char = heapq.heappop(heap)
            res += char
            if prefreq < 0: heapq.heappush(heap,(prefreq,prevChar))
            prefreq, prevChar = freq + 1,char
        if len(res) == len(s): return res
        return ''