class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force: iterate through all the characters until we reach one that either terminates or is not correct
        res = ""
        i = 0
        cur = None
        while True:
            for word in strs:
                if i > len(word)-1:
                    return res
                if not cur:
                    cur = word[i]
                    continue
                if word[i] != cur:
                    return res
            res += cur
            cur = None
            i += 1
        return res
                
            
            