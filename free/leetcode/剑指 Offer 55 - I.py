"""
剑指 Offer 55 - I:输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

 

提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# author: rexdu
# create: 2020/7/28 22:27
from functools import lru_cache


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @lru_cache(1000)
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None and root.right is not None:
            return 1 + self.maxDepth(root.right)
        if root.left is not None and root.right is None:
            return 1 + self.maxDepth(root.left)
        return 1 + self.maxDepth(root.left) if self.maxDepth(root.left) > self.maxDepth(
            root.right) else 1 + self.maxDepth(root.right)
