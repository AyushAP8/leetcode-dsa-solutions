"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

import time

class soln1:
    def binary_search(self, num, target, order):
        start = 0
        end = len(num)//2
        while start <= end:
            mid = (start+end)//2
            print(start, end, mid)
            if num[mid] < target:
                if order == "ascending":
                    start = mid + 1
                else:
                    end = mid - 1
            elif num[mid] > target:
                if order == "ascending":
                    end = mid - 1
                else:
                    start = mid + 1
            elif num[mid] == target:
                return mid
            else:
                return -1


    def first_last_el_pos(self, num, target):
        print(self.binary_search(sorted(num), target, "ascending")) 
        print(self.binary_search(sorted(num, reverse=True), target, "descending")) 
        return [self.binary_search(sorted(num), target, "ascending"), self.binary_search(sorted(num, reverse=True), target, "descending")]

    def search_range(self, nums:list[int], target:int) -> list[int]:
        range = []
        
        if not nums:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        print(start, end)
        while start <= end:
            mid = (start+end)//2
            print(start, end, mid)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] == target:
                range.append(mid)
                break

        if not range:
            return [-1, -1]
        
        while nums[mid] == target:
            if mid < len(nums):
                mid+=1
                if nums[mid] != target:
                    range.append(mid-1)
        
        return range 
         

    test = soln1()
    start = time.perf_counter()
    mp = test.search_range([7, 7, 8, 8, 8, 9, 9, 10], 9)
    end = time.perf_counter()
    print(mp)
    print(f"time = {end - start}")
