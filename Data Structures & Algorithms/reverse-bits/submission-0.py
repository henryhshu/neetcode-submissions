class Solution:
    def reverseBits(self, n: int) -> int:
        # use bit manipulation operations
        # take every bit and & it with a one
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))

        return res