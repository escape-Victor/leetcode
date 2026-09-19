#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = {}
        for i in s:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        for j in t:
            if j in temp:
                temp[j] -= 1
                if temp[j] == 0:
                    del temp[j]
            else:
                return False
        if len(temp) == 0:
            return True
        else:
            return False
# @lc code=end

