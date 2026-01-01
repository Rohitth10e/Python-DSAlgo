def zero_one_knapsack(val, wt, W, n, dp):
    if n==0 or W == 0:
        return 0
        
    if dp[n][W] != -1:
        return dp[n][W]
        
    if wt[n-1] <= W:
        pick = val[n-1] + zero_one_knapsack(val, wt, W-wt[n-1], n-1,dp)
        not_pick = zero_one_knapsack(val, wt, W, n-1,dp)
        
        dp[n][W] = max(pick, not_pick)
    else:
        dp[n][W] = zero_one_knapsack(val, wt, W, n-1,dp)
    return dp[n][W]

wt = [10,20,30]
val = [60,100,120]
W=50
n=len(wt)
dp = [[-1 for _ in range(W+1)] for _ in range(n+1)]
print(zero_one_knapsack(val, wt, W, len(wt),dp))