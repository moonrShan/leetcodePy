class Solution_205:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapStoT = {}
        mapTtoS = {}
        for i in range(0,len(s)):
            charS = s[i]
            charT = t[i]
            if charS not in mapStoT and charT not in mapTtoS:
                mapStoT[charS] = charT
                mapTtoS[charT] = charS
            elif charS in mapStoT and mapStoT[charS] != charT:
                return False
            elif charT in mapTtoS and mapTtoS[charT] != charS:
                return False
        return True


