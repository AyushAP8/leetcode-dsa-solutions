import time

"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109"""

#O(N)
class soln1:
    def duplicate(self, nums: list[int]) -> bool:
        hset = set()
        for i in range(len(nums)):
            if nums[i] in hset:
                return True
            hset.add(nums[i])
        return False
                

test = soln1()

start = time.perf_counter()
mp = test.duplicate([1,1,1,3,3,4,3,2,4,2])
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")