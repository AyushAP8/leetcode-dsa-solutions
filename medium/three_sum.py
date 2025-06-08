"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105"""

import time

#O(N^3)
class soln1:
    def three_sum(self, nums:list[int]) -> list[list[int]]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0 and i!=j and i!=k and j!=k:
                        if sorted([nums[i], nums[j], nums[k]]) not in ans:
                            ans.append(sorted([nums[i], nums[j], nums[k]]))
        return ans

#O(N^2)
class soln2:
    def three_sum(self, nums:list[int]) -> list[list[int]]:
        ans = []
        for i in range(len(nums)):
            target = -nums[i]
            hmp = {}
            for j in range(i+1, len(nums)):
                diff = target-nums[j]
                if diff in hmp:
                    if diff in nums and sorted([-target, nums[j], diff]) not in ans:
                        ans.append(sorted([-target, nums[j], diff]))
                hmp[nums[j]] = j
        return ans

#O(N^2) - optimal
class soln3:
    def three_sum(self, nums:list[int]) -> list[list[int]]:
        ans =[]
        nums.sort()
        for ptr1 in range(len(nums)-2):

            if ptr1>0 and nums[ptr1]==nums[ptr1-1]:
                continue
            ptr2, ptr3 = ptr1+1, len(nums)-1

            while(ptr2<ptr3):
                if nums[ptr1]+nums[ptr2]+nums[ptr3] == 0:
                    ans.append([nums[ptr1],nums[ptr2],nums[ptr3]])
                    ptr3-=1
                    while ptr2<ptr3 and nums[ptr3]==nums[ptr3+1]:
                        ptr3-=1
                elif nums[ptr1]+nums[ptr2]+nums[ptr3]>0:
                    ptr3-=1
                else:
                    ptr2+=1
        return ans

nums = [-1,0,1,2,-1,-4]
test = soln3()
start = time.perf_counter()
ans = test.three_sum(nums)
end = time.perf_counter()
print(f"\n{ans}")
print(f"time = {end-start}")