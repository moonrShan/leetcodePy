class Solution_486:
    def __init__(self):
        self.memo = {}  # initial value + nums + order -> win or not

    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.PredictTheWinnerGeneral(0, 0, True, nums)

    def PredictTheWinnerGeneral(self, player1Score: int, player2Score: int, player1Start: bool,
                                nums: List[int]) -> bool:
        numsTuple = tuple(nums)
        if (player1Score, player2Score, player1Start, numsTuple) in self.memo:
            return self.memo[(player1Score, player2Score, player1Start, numsTuple)]

        if not nums:
            return player1Score >= player2Score

        if player1Start:
            pickResult = False
            pickResult |= self.PredictTheWinnerGeneral(player1Score + nums[0], player2Score, False, nums[1:])
            pickResult |= self.PredictTheWinnerGeneral(player1Score + nums[-1], player2Score, False,
                                                       nums[:len(nums) - 1])
        else:
            pickResult = True
            pickResult &= self.PredictTheWinnerGeneral(player1Score, player2Score + nums[0], True, nums[1:])
            pickResult &= self.PredictTheWinnerGeneral(player1Score, player2Score + nums[-1], True,
                                                       nums[:len(nums) - 1])

        self.memo[(player1Score, player2Score, player1Start, numsTuple)] = pickResult

        return pickResult