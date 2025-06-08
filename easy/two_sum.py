"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?"""

import time

#O(N^2) - 30ms
class soln1:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#O(N) - 68ms
class soln2:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        '''Runtime: 52 ms, faster than 99.72% of Python3 online submissions for Two Sum.
        Memory Usage: 15.3 MB, less than 24.50% of Python3 online submissions for Two Sum.'''
        hmp = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hmp:
                return [hmp[diff],i]
            hmp[num]=i

#O(N)
class soln3:
    '''problem with duplicate value'''
    def two_sum(self, nums:list[int], target:int) -> list[int]:
        hmp = {}
        for i, num in enumerate(nums):
            hmp[num]=i
        nums.sort()
        ptr1 = 0
        ptr2 = len(nums)-1
        while ptr1<ptr2:
            if nums[ptr1] + nums[ptr2] == target:
                return [hmp[nums[ptr1]],hmp[nums[ptr2]]]
            elif nums[ptr1] + nums[ptr2] < target:
                ptr1+=1
            else:
                ptr2-=1

                

test = soln2()

start = time.perf_counter()
mp = test.two_sum([3,4,5,2,3], 9)
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")



