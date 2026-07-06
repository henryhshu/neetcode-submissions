class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquared(n):
            s = 0
            while n:
                s += (n % 10)**2
                n = n // 10
            return s

        visited = set()
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            n = sumSquared(n)

        return False