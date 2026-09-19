#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        cnt = Counter(nums)
        n = len(nums)
        buckets = [[] for i in range(n + 1)]
        for num, freq in cnt.items():
            buckets[freq].append(num)
        res = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
# @lc code=end

