class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        curr = 0
        i1, i2 = 0, 0
        while i1 < m and i2 < n:
            if nums1[i1] <= nums2[i2]:
                temp.append(nums1[i1])
                i1 += 1
            else:
                temp.append(nums2[i2])
                i2 += 1
        temp += nums1[i1:m]
        temp += nums2[i2:n]
        for i in range(len(nums1)):
            nums1[i] = temp[i]


            

        
            
