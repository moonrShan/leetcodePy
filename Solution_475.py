class Solution_475:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        result = 0
        for house in houses:
            result = max(result, self.radius(house, heaters))
        return result

    def radius(self, target, heaters):
        left, right = 0, len(heaters) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if heaters[mid] == target:
                return 0
            if heaters[mid] > target:
                right = mid
            if heaters[mid] < target:
                left = mid
        return min(abs(heaters[right] - target), abs(target - heaters[left]))
