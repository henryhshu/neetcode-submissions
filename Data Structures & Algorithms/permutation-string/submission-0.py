class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, count2 = [0] * 26, [0] * 26
        # initialize count1 and count2
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1
        # count matches
        matches = 0
        for i in range(len(count1)):
            if count2[i] == count1[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            i = ord(s2[r]) - ord("a")
            count2[i] += 1
            if count1[i] == count2[i]:
                matches += 1
            elif count1[i] + 1 == count2[i]:
                matches -= 1
            
            i = ord(s2[l]) - ord("a")
            count2[i] -= 1
            if count1[i] == count2[i]:
                matches += 1
            elif count1[i] - 1 == count2[i]:
                matches -= 1
            l += 1
        return matches == 26