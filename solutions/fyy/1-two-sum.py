#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hash:
                index = [i, hash.get(target - nums[i])]
                return index
            else:
                hash.setdefault(nums[i], i)

# @lc code=end

