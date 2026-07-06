class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we can recursively break down if a position is possible
        # can cache the result at each index
        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]