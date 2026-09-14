class Solution:

    def minimum_cost(self, i, cost: List[int], memo = None):
        if memo is None:
            memo = {}
        
        if i in memo:
            return memo[i]
        if i >= len(cost):
            return 0

        res = cost[i] + min(
            self.minimum_cost(i + 1, cost, memo),
            self.minimum_cost(i + 2, cost, memo)
        )
        memo[i] = res
        return res



    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res_0 = self.minimum_cost(0, cost)
        res_1 = self.minimum_cost(1, cost)
        return min(res_0, res_1)

        