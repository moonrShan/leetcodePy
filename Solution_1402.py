class Solution_1402:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        nonNegetiveDish = []
        negativeDish = []
        for s in satisfaction:
            if s >= 0:
                nonNegetiveDish.append(s)
            else:
                negativeDish.append(s)
        nonNegetiveDish.sort()
        negativeDish.sort(reverse=True)

        totalnonNegetiveCount = sum(nonNegetiveDish)
        currentOrder = nonNegetiveDish

        for dish in negativeDish:
            if dish + totalnonNegetiveCount > 0:
                currentOrder = [dish] + currentOrder
                totalnonNegetiveCount += dish
            else:
                break
        return sum([(i + 1) * currentOrder[i] for i in range(len(currentOrder))])

