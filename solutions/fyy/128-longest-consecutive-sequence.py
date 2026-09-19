#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        l = set(nums)
        length = 0
        for i in l:
            if (i - 1) in l:
                continue
            else:
                temp = 1
                j = i + 1
                while j in l:
                    temp += 1
                    j += 1
                if temp > length:
                    length = temp
        return length


# @lc code=end

