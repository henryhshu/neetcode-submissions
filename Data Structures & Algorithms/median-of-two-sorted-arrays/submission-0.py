class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # how median is defined: middle of list if odd, average of the two middle values if even
        # brute force is to merge them and then find the median which is O(N) time
        # we likely need to use some variation of binary search, we can use a binary partition
        # we start from the first index in nums1, binary search until the sum of the size of the partitions are equal
        # to do this, we must satisfy the condition where nums1[i] >= nums2[j-1] and nums1[i-1] >= nums2[j]
        
        # make sure we run binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # run the binary search
        total = len(nums1) + len(nums2)
        half = total // 2
        l, r = 0, len(nums1)-1
        while True:
            i = (l+r)//2
            j = half - i - 2
            left1 = nums1[i] if i >= 0 else -float("inf")
            right1 = nums1[i+1] if i+1 < len(nums1) else float("inf")
            left2 = nums2[j] if j >= 0 else -float("inf")
            right2 = nums2[j+1] if j+1 < len(nums2) else float("inf")
            if left1 <= right2 and right1 >= left2:
                if total % 2:
                    # the left partition will always be the smaller one, so we take the min of the right partition
                    return min(right1, right2)
                else:
                    return (max(left1,left2) + min(right1,right2)) / 2
            elif left1 > right2:
                r = i-1
            else:
                l = i+1

