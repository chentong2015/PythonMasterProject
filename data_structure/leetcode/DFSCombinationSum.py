class Solution(object):

    """
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation: These are the only two combinations.
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.

    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def combination_sum(self, candidates, target):
        result = []
        self.dfs(candidates, target, [], result)
        candidates.sort()
        print(candidates)

    # TODO. DFS 深度优先变量需要将最后的结果作为参数传递
    def dfs(self, nums, target, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+nums[[i]], result)


if __name__ == '__main__':
    solution = Solution()
    solution.combination_sum([10, 7, 9, 2, 5], 5)
