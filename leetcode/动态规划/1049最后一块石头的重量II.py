'''

输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

石头总重为all，分成两组石头a和b，a的重量为x，
b的重量为all-x，要使两组之间差距最小，则all-x-x的值要趋于0

只要找到a组的重量，接近x，既all/2
求将一堆石头，放入容量为all/2，最大的重量
最终的结果是要乘2
'''

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # stones_sum = sum(stones)
        target = sum(stones) / 2
        res = self.process(0, stones, target)
        print(res * 2)

    def process(self, index, stones, target):
        if index == len(stones):
            return target

        if target - stones[index] < 0:
            return self.process(index + 1, stones, target)

        p1 = self.process(index + 1, stones, target - stones[index])
        p2 = self.process(index + 1, stones, target)
        return min(p1, p2)


if __name__ == '__main__':
    s = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    stones = [31, 26, 33, 21, 40]
    s.lastStoneWeightII(stones)
