class Solution_3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        apperIndexDict = {} #char to int
        while right < len(s):
            if s[right] not in apperIndexDict.keys() or apperIndexDict[s[right]] < left:
                result = max(result, right - left + 1)
            else:
                left = apperIndexDict[s[right]] + 1
            apperIndexDict[s[right]] = right
            right += 1
        return result