class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        brute force is to one pass to count up all the elements into a hashmap
        turn it into a list then sort the list and return the top k elements
        """
        numsDict = defaultdict(int)
        for num in nums:
            numsDict[num] += 1
        freq = [[] for i in range(len(nums)+1)]
        for num, count in numsDict.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res