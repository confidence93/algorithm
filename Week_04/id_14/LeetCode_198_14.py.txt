class Solution:
    # dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        p = nums[0]
        q = max(nums[0],nums[1])
        
        
        for i in range(2,n):
            next_ = max(p+nums[i],q)
            p,q = q, next_
            
        return q
