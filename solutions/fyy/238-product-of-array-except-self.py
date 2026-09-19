#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = [1]
        right = [1]
        product = []
        length = len(nums)
        for i in range(1, length):
            left.append(left[i - 1] * nums[i - 1])
            right.append(right[i - 1] * nums[length - i])
        for i in range(length):
            product.append(left[i] * right[length - i - 1])
        return product
# @lc code=end

