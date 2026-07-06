class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # sliding window solution from l to r
        l, r = 0, 1
        res, prev = 1, ""
        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                r += 1
                res = max(res, r - l)
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                r += 1
                res = max(res, r - l)
                prev = "<"
            else:
                r = r+1 if arr[r] == arr[r-1] else r
                l = r - 1
                prev = ""
        return res
