class Solution_838:
    def pushDominoes(self, dominoes: str) -> str:
        dominoesList = list(dominoes)
        queue = []
        n = len(dominoesList)
        for i,direction in enumerate(dominoesList):
            if (direction != '.' ):
                queue.append(i)

        while queue:
            nextDominoesList = list(dominoesList)
            for c in range(len(queue)):
                i = queue.pop(0)
                direction = dominoesList[i]
                if (direction == 'R' and (i < n-1 and dominoesList[i+1] == '.') and (i > n-3 or dominoesList[i+2] != 'L')):
                    nextDominoesList[i+1] = 'R'
                    queue.append(i+1)
                if (direction == 'L' and (i > 0 and dominoesList[i-1] == '.') and (i < 2 or dominoesList[i-2] != 'R' )):
                    nextDominoesList[i-1] = 'L'
                    queue.append(i-1)
            dominoesList = nextDominoesList
        return ''.join(dominoesList)