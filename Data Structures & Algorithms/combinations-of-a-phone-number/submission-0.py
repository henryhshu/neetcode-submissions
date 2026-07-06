class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtracking(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for char in digitsChar[digits[i]]:
                backtracking(i+1, curr+char)
        if digits:
            backtracking(0, "")
        return res