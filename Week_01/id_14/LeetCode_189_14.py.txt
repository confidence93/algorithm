class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        for i in xrange(0, k):
            tmp = nums[-1]
            for j in xrange(0, len(nums) - 1):
                nums[len(nums) - 1 - j] = nums[len(nums) - 2 - j]
            nums[0] = tmp