class Solution_394:
    def decodeString(self, s: str) -> str:
        result = ''
        i, nums, n = 0, 0, len(s)
        while i < n:
            if s[i].isdigit():
                nums = nums * 10 + int(s[i])
                i += 1
            elif s[i].isalpha():
                result += s[i]
                i += 1
            elif s[i] == '[':
                countLeft = 1
                j = i + 1
                while j < n:
                    if s[j] == '[':
                        countLeft += 1
                    elif s[j] == ']':
                        countLeft -= 1
                    if countLeft == 0:
                        result += max(nums, 1) * self.decodeString(s[i+1:j])
                        nums = 0
                        break
                    j += 1
                i = j + 1
        return result
