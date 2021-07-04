# 1911. Maximum Alternating Subsequence Sum
# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

'''
原先思路：
  求解所有的子序列（一共2^n个）的alternating sum，返回最大的一个
原先思路的问题：
  子序列数量过多导致超时（题目里n的规模是10^5）
正确思路：
  动态规划，遍历一次输入序列即可。
  对于已经遍历过的i个，用两个变量odd和even代表当前所有可能的子序列里最大的alternating sum。
    odd：所有可能的，奇数个元素的子序列，能产生的最大的alternating sum
    even：所有可能的，偶数个元素的子序列，能产生的最大的alternating sum
  对于第i+1个元素，利用当前的odd和even来更新结果
  最后返回odd
'''
class Solution:
    def maxAlternatingSum(self, A: List[int]) -> int:
        odd = even = 0
        for a in A:
            odd, even = max(even + a, odd), max(odd - a, even)
        return odd
