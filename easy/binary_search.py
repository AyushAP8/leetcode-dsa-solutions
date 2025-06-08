import time

'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

class soln1:
    def binary_search(self, nums: list[int], target: int) -> int:
        '''Runtime: 272 ms, faster than 79.62% of Python3 online submissions for Binary Search.
        Memory Usage: 15.5 MB, less than 72.10% of Python3 online submissions for Binary Search.
        '''
        lptr, rptr = 0, len(nums)
        while lptr <= rptr:
            mid = lptr + ((rptr - 1) // 2) #https://stackoverflow.com/questions/6735259/calculating-mid-in-binary-search - l + r) // 2 can lead to overflow
            if lptr <= mid >= rptr:
                return -1
            elif nums[mid] < target:
                lptr += 1
            elif nums[mid] > target:
                rptr -= 1
            else:
                return mid
            
            
test = soln1()
start_time = time.perf_counter()
ans = test.binary_search([-1, 0, 3, 5, 9, 12], 13)
print(f"ans = {ans}, time = {time.perf_counter() - start_time}")