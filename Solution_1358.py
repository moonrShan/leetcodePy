class Solution_1358:
    # not me
    def numberOfSubstrings(self, s: str) -> int:
        ans, lo, cnt = 0, -1, {c: 0 for c in 'abc'}
        for hi, c in enumerate(s):
            cnt[c] += 1
            while all(cnt.values()):
                ans += len(s) - hi
                lo += 1
                cnt[s[lo]] -= 1
        return ans
