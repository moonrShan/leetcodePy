class Solution_1103:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result, turn = [0] * num_people, 0
        while candies > num_people * (1 + num_people) // 2 + turn * num_people * num_people:
            for i in range(1, num_people+1):
                given = i + turn * num_people
                result[i-1] += given
                candies -= given
            turn += 1
        for i in range(1, num_people+1):
            if candies > i + turn * num_people:
                given = i + turn * num_people
                result[i-1] += given
                candies -= given
            else:
                result[i-1] += candies
                break
        return result