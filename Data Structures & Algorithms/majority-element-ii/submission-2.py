
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # observations:
        #   maximum number of majority elements is 2
        #   brute force: use one pass counter
        # optimized: use a hashmap of size 2 to be constant time
        # decrement all the elements in the hashmap whenever the size of the hashmap becomes 3
        
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if len(counter) <= 2:
                continue
            new_counter = defaultdict(int)
            for n, c in counter.items():
                if c > 1:
                    new_counter[n] = c - 1 # only add to new counter if the count is greater than 0
            counter = new_counter
        # resulting size of counter will be less than 3
        # check to see if the candidates are thirds majority
        res = []
        for n in counter:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res