class Solution_1629:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        answer = keysPressed[0]
        releaseTime = releaseTimes[0]
        for i in range(1,len(keysPressed)):
            if releaseTimes[i] - releaseTimes[i-1] > releaseTime:
                answer = keysPressed[i]
                releaseTime = releaseTimes[i] - releaseTimes[i-1]
            elif releaseTimes[i] - releaseTimes[i-1] == releaseTime and keysPressed[i] > answer:
                answer = keysPressed[i]
                releaseTime = releaseTimes[i] - releaseTimes[i-1]
        return answer