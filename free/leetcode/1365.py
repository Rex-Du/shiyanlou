"""
1365:给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。

 

示例 1：

输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释：
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。
对于 nums[3]=2 存在一个比它小的数字：（1）。
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
示例 2：

输入：nums = [6,5,4,8]
输出：[2,1,0,3]
示例 3：

输入：nums = [7,7,7,7]
输出：[0,0,0,0]
 

提示：

2 <= nums.length <= 500
0 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# author: rexdu
# create: 2020/8/6 22:50
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # n ** 2
        # n = len(nums)
        # ret = list()
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if j != i and nums[j] < nums[i]:
        #             count += 1
        #     ret.append(count)
        # return ret
        # 题目中 0 <= nums[i] <= 100,定义一个列表，存放每个数字出现的频率
        freq = [0] * 101
        # 统计nums中每个数字出现的频率，如10出现了5次，那么freq[10] = 5
        for i in nums:
            freq[i] += 1
        # 统计比当前值小的次数和
        for i in range(1, 101):
            freq[i] += freq[i - 1]
        ret = list()
        for i in nums:
            if i > 0:
                ret.append(freq[i-1])
            else:
                ret.append(0)
        return ret

    if __name__ == '__main__':
        s = Solution()
        print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
