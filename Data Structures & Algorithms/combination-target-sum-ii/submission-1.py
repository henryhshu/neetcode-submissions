class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(i, cur, total):
            if total == target:
                res.add(tuple(sorted(cur.copy())))
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        res = [list(combo) for combo in res]
        return res