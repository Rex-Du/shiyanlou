# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 256 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [i.lower() for i in s if i in string.ascii_letters or i in string.digits] == [i.lower() for i in s if i in string.ascii_letters or i in string.digits][::-1]
# leetcode submit region end(Prohibit modification and deletion)
