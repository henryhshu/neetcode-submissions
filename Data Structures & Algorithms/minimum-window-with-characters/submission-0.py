class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = defaultdict(int), defaultdict(int)
        for char in t:
            countT[char] += 1

        l = 0
        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(countT)
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] += 1
                if window[s[r]] == countT[s[r]]:
                    have += 1

            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""
            
        