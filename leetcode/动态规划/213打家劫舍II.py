"""
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        意味着第一个房子和最后一个房子中 只能选择一个偷窃，
        因此可以把此 环状排列房间 问题约化为两个 单排排列房间 子问题
        1、在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1
        2、在不偷窃最后一个房子的情况下（即 nums[:n−1]），最大金额是 p2
        为以上两种情况的较大值
        '''
        p1 = self.f(0, nums)
        p2 = self.g(1, nums)
        res = max(p1, p2)
        print(res)

    def f(self, index, nums):
        """
        偷第一家 (0 ~ n-2)
        :param index:
        :param nums:
        :return:
        """
        if index == len(nums) - 1:
            return 0
        if index == len(nums) - 2:
            return nums[index]
        return max(self.f(index + 1, nums), self.f(index + 2, nums) + nums[index])

    def g(self, index, nums):
        """
        不偷第一家 (1 ~ n-1)
        :param index:
        :param nums:
        :return:
        """
        if index == len(nums):
            return 0
        if index == len(nums) - 1:
            return nums[index]
        return max(self.g(index + 1, nums), self.g(index + 2, nums) + nums[index])


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3,1]
    # nums = [2, 3, 1]
    s.rob(nums)
