class Solution_189:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in range(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
            n, j = n - k, j + k
            k = k % n