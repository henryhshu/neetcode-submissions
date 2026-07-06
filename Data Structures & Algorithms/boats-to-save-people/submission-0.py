class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the input to try and pair heaviest with lightest
        # use two pointer approach
        # loop while l <= r
        # maintain count of current boats
        boats = 0
        people.sort()
        l, r = 0, len(people)-1
        while l <= r:
            if people[l] + people[r] <= limit:
                # heaviest and lightest can optimally fit in one boat
                boats += 1
                l += 1
                r -= 1
            else:
                # only current heaviest can be saved
                boats += 1
                r -= 1
        return boats

