"""
1299:给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。

完成所有替换操作后，请你返回这个数组。

 

示例：

输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]
 

提示：

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# author: rexdu
# create: 2020/7/28 22:51
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = list()
        n = arr.__len__() - 1
        max_ = -1
        while n >= 0:
            ret.insert(0, max_)
            if arr[n] > max_:
                max_ = arr[n]
            n -= 1
        return ret
