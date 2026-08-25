class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = {}
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in sl:
                l = max(sl[s[r]] + 1, l)
            sl[s[r]] = r
            result = max(result, r-l+1)
        return result