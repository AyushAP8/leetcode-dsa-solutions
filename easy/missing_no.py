import time

'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
class soln1:
    '''Runtime: 3477 ms, faster than 11.66% of Python3 online submissions for Missing Number.
    Memory Usage: 15.5 MB, less than 13.45% of Python3 online submissions for Missing Number.
    Ans = 2, Time taken = 1.2199999999989997e-05
    Ans = 2, Time taken = 1.980000000001425e-05        
    Ans = 8, Time taken = 1.4199999999991997e-05'''
    def missing_number(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
                
                
class soln2:
    def missing_number(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += 1
        return res

    
class soln3:
    def missing_number(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i < len(nums):
                res = i ^ nums[i]
            else:
                res = i ^ 0
        return res
            
class soln3:
    def missing_number(self, nums: list[int]) -> int:
        res = 0
        i = 0
        while i != len(nums) + 1:
            print(res)
            if i < len(nums): 
                res = i ^ nums[i]
            else:
                res = res ^ i
            i += 1
        return res
    
class soln4:
    def missing_number(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += i - nums[i]
        return res + i + 1
    
test = soln4()    
start_time = time.perf_counter()
ans = test.missing_number([3,0,1])
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.missing_number([0,1])
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.missing_number([9,6,4,2,3,5,7,0,1])
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")