class Solution_2060:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        s1Permuataion = self.candidatePermutation(self.parseString(s1))
        s2Permuataion = self.candidatePermutation(self.parseString(s2))
        candidates = self.candidatePair(s1Permuataion, s2Permuataion)
        for candidate in candidates:
            s1Can, s2Can = candidate
            if self.checkMatch(tuple(s1Can), tuple(s2Can)):
                return True
        return False

    @cache
    def checkMatch(self, s1, s2):
        s1, s2 = list(s1), list(s2)
        if not s1 and not s2:
            return True
        if (not s1 or not s2) and (len(s1) + len(s2)):
            return False
        if str(s1[0])[0].isalpha() and str(s2[0])[0].isalpha():
            lenS1 = len(str(s1[0]))
            lenS2 = len(str(s2[0]))
            if lenS1 < lenS2:
                return s1[0] == s2[0][:lenS1] and self.checkMatch(tuple(s1[1:]), tuple([s2[0][lenS1:]] + s2[1:]))
            elif lenS1 > lenS2:
                return s2[0] == s1[0][:lenS2] and self.checkMatch(tuple([s1[0][lenS2:]] + s1[1:]), tuple(s2[1:]))
            else:
                return s1[0] == s2[0] and self.checkMatch(tuple(s1[1:]), tuple(s2[1:]))

        if not str(s1[0])[0].isalpha() and not str(s2[0])[0].isalpha():
            lenS1 = s1[0]
            lenS2 = s2[0]
            if lenS1 < lenS2:
                return self.checkMatch(tuple(s1[1:]), tuple([s2[0] - lenS1] + s2[1:]))
            elif lenS1 > lenS2:
                return self.checkMatch(tuple([s1[0] - lenS2] + s1[1:]), tuple(s2[1:]))
            else:
                return self.checkMatch(tuple(s1[1:]), tuple(s2[1:]))

        if str(s1[0])[0].isalpha() and len(s1[0]) < s2[0]:
            return self.checkMatch(tuple(s1[1:]), tuple([s2[0] - len(s1[0])] + s2[1:]))
        if str(s1[0])[0].isalpha() and len(s1[0]) == s2[0]:
            return self.checkMatch(tuple(s1[1:]), tuple(s2[1:]))
        if str(s1[0])[0].isalpha() and len(s1[0]) > s2[0]:
            return self.checkMatch(tuple([s1[0][s2[0]:]] + s1[1:]), tuple(s2[1:]))

        if str(s2[0])[0].isalpha() and len(s2[0]) < s1[0]:
            return self.checkMatch(tuple([s1[0] - len(s2[0])] + s1[1:]), tuple(s2[1:]))
        if str(s2[0])[0].isalpha() and len(s2[0]) == s1[0]:
            return self.checkMatch(tuple(s1[1:]), tuple(s2[1:]))
        if str(s2[0])[0].isalpha() and len(s2[0]) > s1[0]:
            return self.checkMatch(tuple(s1[1:]), tuple([s2[0][:s1[0]]] + s2[1:]))

    def candidatePair(self, s1Permuataions, s2Permuataions):
        s1Dict = collections.defaultdict(list)
        s2Dict = collections.defaultdict(list)
        for s1P in s1Permuataions:
            s1Dict[self.countLength(s1P)].append(s1P)
        for s2P in s2Permuataions:
            s2Dict[self.countLength(s2P)].append(s2P)

        result = []
        for k, s1Candidates in s1Dict.items():
            s2Candidates = s2Dict[k]
            for s2Candidate in s2Candidates:
                for s1Candidate in s1Candidates:
                    result.append([s1Candidate, s2Candidate])
        return result

    def countLength(self, permutaion):
        count = 0
        for p in permutaion:
            if str(p)[0].isalpha():
                count += len(p)
            else:
                count += int(p)
        return count

    def parseString(self, s):
        result = []
        flag = s[0].isalpha()
        current = ''
        for c in s:
            currentFlag = c.isalpha()
            if currentFlag == flag:
                current += c
            else:
                result.append(current)
                current = c
                flag = currentFlag
        result.append(current)
        return result

    def candidatePermutation(self, candidateList):
        result = [[]]
        for i, part in enumerate(candidateList):
            temp = []
            for child in self.parsePart(part):
                for each in result:
                    temp.append(each + [child])
            result = temp
        return result

    def parsePart(self, num):
        result = []
        if num[0].isalpha():
            return [num]
        if len(num) == 1:
            result.append(int(num))
        if len(num) == 2:
            result.append(int(num[0]) + int(num[1]))
            result.append(int(num))
        if len(num) == 3:
            result.append(int(num[0]) + int(num[1]) + int(num[2]))
            result.append(int(num[0] + num[1]) + int(num[2]))
            result.append(int(num[0]) + int(num[1] + num[2]))
            result.append(int(num))
        result = list(set(result))
        return result