class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) <= 3:
            return max(nums)
        a = [0] * (len(nums) - 1)
        for i,j in enumerate(nums[1:]):
            if i == 0:
                a[0] = nums[1]
                continue
            a[i] = max(a[i - 1], a[i - 2] + j)
        maxv = a[-1]
        a = [0] * (len(nums) - 1)
        for i,j in enumerate(nums[:-1]):
            if i == 0:
                a[0] = nums[0]
                continue
            a[i] = max(a[i - 1], a[i - 2] + j)
        return max(a[-1], maxv)
