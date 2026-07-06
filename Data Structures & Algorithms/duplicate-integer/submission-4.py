class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for i in nums:
            if i in temp:
                return True
            else:
                temp.add(i)
        return False