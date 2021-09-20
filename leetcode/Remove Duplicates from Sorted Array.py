https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# 정렬, 중복 없애기
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        result = len(nums) 
        return result
      
