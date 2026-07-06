class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # keep track of how much change we have
        # iterate through all the customers to see if we can provide them with their change
        # we can also just keep track of all the bills we have in a hashmap
        wallet = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 5:
                wallet[5] += 1
            elif bill == 10:
                if wallet[5] == 0:
                    return False
                wallet[5] -= 1
                wallet[10] += 1
            else:
                # bill is 20
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1
                    wallet[5] -= 1
                    wallet[20] += 1
                    continue
                if wallet[5] < 3:
                    return False
                else:
                    wallet[5] -= 3
                    wallet[20] += 1
        return True
            