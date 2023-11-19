class Solution(object):
    """
    Given an array of integers nums and an integer target,
    Return indices of the two numbers such that they add up to target.
    1. Each input would have exactly one solution
    2. You may not use the same element twice
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    def two_sum(self, nums, target):
        results = []
        left = 0
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                break
            elif total < target:
                left = left + 1
            else:
                right = right - 1
        results.append(left)
        results.append(right)
        return results


if __name__ == '__main__':
    solution = Solution()
    result = solution.two_sum([2, 12, 7, 11], 9)
    print(result)