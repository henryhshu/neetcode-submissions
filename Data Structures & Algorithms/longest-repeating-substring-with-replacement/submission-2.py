class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find longest repeating after replacing k chars
        # sliding window and hashmap for each capital letter
        freqs = defaultdict(int)
        res = 0
        l, r = 0, 0
        for r in range(len(s)):
            tmp = max(freqs.values()) if freqs else 0
            freqs[s[r]] += 1

            while (r-l+1) - max(freqs.values()) > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res