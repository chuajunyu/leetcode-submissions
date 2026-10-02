class Solution:
    def rob(self, nums: list[int]) -> int:
        # dp array where dp[x] is the max amount of money you can make if you robbed this house x

        dp = list(nums)

        if len(dp) <= 2:
            return max(dp)
        
        if len(dp) == 3:
            return max(dp[1], dp[0] + dp[2])
        
        dp[2] = max(dp[1], dp[0] + dp[2])
        for i in range(3, len(dp)):
            # the max amount you can get at this house is by robbing this house 
            dp[i] = max(dp[i] + dp[i - 2], dp[i] + dp[i - 3])

        print(dp)
        
        return max(dp[-1], dp[-2])
        