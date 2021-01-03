# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 464 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def search(n, k, i, cur):
            res = []

            if len(cur) == k:
                return [cur[:]]
            if i == n + 1:
                return []

            res.extend(search(n, k, i + 1, cur))

            cur.append(i)
            res.extend(search(n, k, i + 1, cur))
            cur.pop()
            return res

        return search(n, k, 1, [])
# leetcode submit region end(Prohibit modification and deletion)
