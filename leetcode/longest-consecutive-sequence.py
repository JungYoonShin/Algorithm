class Solution(object):
  def longestConsecutive(self, nums):
      new_nums = set(nums)
      max_count = 0
      for num in new_nums:
          if num-1 not in new_nums:
              count = 1
              while num+1 in new_nums:
                  num+=1
                  count += 1
              max_count = max(max_count, count)
      return max_count

#671ms Beats 43.56%