import time

'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

class soln1:
    '''Runtime: 190 ms, faster than 67.17% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 50.74% of Python3 online submissions for Single Number.
Ans = 1, Time taken = 3.4000000000006247e-06
Ans = 4, Time taken = 4.700000000003313e-06        
Ans = 1, Time taken = 4.599999999993498e-06  
    '''
    def single_number(self, nums: list[int]) -> int:
        xor_res = 0
        for n in nums:
            xor_res = n ^ xor_res
        return xor_res
    
test = soln1()

start_time = time.perf_counter()
ans = test.single_number([2,2,1])
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.single_number([4,1,2,1,2])
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.single_number([1])
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")