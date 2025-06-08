import time

'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

class soln1:
    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1 + self.climb_stairs(1)
        if n > 2:
            return 1 + self.climb_stairs(n - 1) + 2 + self.climb_stairs(n - 2)
        

#O(2^n) - brute force approach        
class soln2:
    '''Time Limit Exceeded'''
    def track_climb_stairs(self, i: int, n: int) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        return self.track_climb_stairs(i + 1, n) + self.track_climb_stairs(i + 2, n)
        
    def climb_stairs(self, n: int) -> int:
        return self.track_climb_stairs(0, n)

#dynamic p
class soln3:
    def climb_stairs(self, n: int) -> int:
        '''Runtime: 39 ms, faster than 70.56% of Python3 online submissions for Climbing Stairs.
        Memory Usage: 13.9 MB, less than 56.86% of Python3 online submissions for Climbing Stairs.
        '''
        temp1, temp2 = 1, 1
        for i in range(n - 1):
            sum = temp1 + temp2
            temp1 = temp2
            temp2 = sum
        return temp2

#dynamic p
class soln4:
    def climb_stairs(self, n: int) -> int:
        '''Runtime: 39 ms, faster than 70.56% of Python3 online submissions for Climbing Stairs.
        Memory Usage: 14 MB, less than 11.65% of Python3 online submissions for Climbing Stairs.
        '''
        if n <= 3:
            return n
        temp1, temp2 = 2, 3
        for i in range(4, n + 1):
            sum = temp1 + temp2
            temp1 = temp2
            temp2 = sum
        return temp2

        
test = soln2()

start_time = time.perf_counter()
ans = test.climb_stairs(1)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.climb_stairs(2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.climb_stairs(3)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.climb_stairs(4)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.climb_stairs(5)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")