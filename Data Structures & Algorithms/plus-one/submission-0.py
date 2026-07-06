class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        res = digits[::-1]
        for i in range(len(res)):
            if res[i] < 9:
                res[i] += 1
                return res[::-1]
            else:
                carry = True
                res[i] = 0
        if carry:
            res.append(1)
        return res[::-1]