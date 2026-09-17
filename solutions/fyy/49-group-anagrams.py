#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in group:
                group[key].append(i)
            else:
                group[key] = [i]
        return list(group.values())
# @lc code=end

