# 1921. Eliminate Maximum Number of Monsters
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

'''
原先思路：
  贪心法。计算最先到达的次序，放入堆中，依次删除堆顶元素。
  每次删除时更新其他元素距离，若发现存在距离非正，则返回删除的元素个数。
原先思路的问题：
  每次删除时都要修改其余元素，时间开销过大导致超时。
  最坏时间复杂度达到O(N^2logN)
正确思路：
  按照到达时间排序，在时间戳0,1,2,...依次消除。
  若时间戳小于到达时间，则说明在到达之前可以消除。反之则无法消除，返回已消除元素个数后结束。
  最坏时间复杂度降至O(NlogN)
'''
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time_cost = [d / s for d, s in zip(dist, speed)]
        
        res = 0
        for i, t in enumerate(sorted(time_cost)):
            if i < t:
                res += 1
            else:
                break
        return res
