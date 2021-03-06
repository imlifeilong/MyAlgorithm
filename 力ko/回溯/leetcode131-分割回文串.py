from typing import List

'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成

'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.dfs(0, s, [])
        return self.result

    # def is_palindrome(self, string):
    #     '''判断是否回文'''
    #     lenght = len(string)
    #     for i in range(lenght):
    #         if string[i] != string[-i - 1]:
    #             return False
    #     return True
    def is_palindrome(self, string):
        '''判断是否回文'''
        return True if string == string[::-1] else False

    def dfs(self, index, string, tmp):

        # 字符串已经切割完，记录最终状态
        if not string:
            self.result.append(tmp.copy())
            return

        for i in range(len(string)):
            substr = string[:i + 1]
            print(index, substr)
            # 判断当前子集是否是回文
            if self.is_palindrome(substr):
                # 如果是回文串 记录下
                tmp.append(substr)
                # 接着递归接下来的字符串
                self.dfs(index + 1, string[i + 1:], tmp)
                # 回溯
                tmp.pop()


if __name__ == '__main__':
    st = 'aab'
    s = Solution()
    print(s.partition(st))

    ''' 横向遍历
    纵                aab
    向              /  |  \ 
    递             /   |   X   剪枝 
    归           a     aa  aab
    遍          / X   /
    历         a  ab b
              / 
             b    
    '''
