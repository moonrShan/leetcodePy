class Solution_373:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        visited = set()
        heap = []
        output = []
        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        while len(output) < k and heap:
            val = heappop(heap)
            output.append((nums1[val[1]], nums2[val[2]]))
            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
                visited.add((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heappush(heap, (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))
                visited.add((val[1], val[2] + 1))

        return output