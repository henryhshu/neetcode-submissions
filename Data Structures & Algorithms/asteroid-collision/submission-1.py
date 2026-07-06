class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Each direction moves at the same speed,
        # meaning they can be processed sequentially.
        # asteroids moving in same direction will never meet
        # only evaluate asteroids that start positive, evaluate when hit negative asteroid
        stack = []
        for a in asteroids:
            add = True
            while stack and a < 0 and stack[-1] > 0: # collision occurs
                diff = stack[-1] + a
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    add = False
                    break
                else:
                    stack.pop()
                    add = False
                    break
            if add:
                stack.append(a)
        return stack
                    

