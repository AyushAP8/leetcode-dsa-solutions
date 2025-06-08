from memory_profiler import profile
import time

'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
'''

class soln1:
    '''Runtime error: time limit exceeded
    Ans = True, Time taken = 2.0800000000001373e-05
    Ans = True, Time taken = 2.4999999999997247e-05    
    Ans = True, Time taken = 2.1199999999998997e-05'''
    def is_happy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
            if n == 1:
                return True
        return False
            
class soln2:
    '''Runtime: 61 ms, faster than 34.10% of Python3 online submissions for Happy Number.
    Memory Usage: 13.9 MB, less than 14.36% of Python3 online submissions for Happy Number.
    Ans = True, Time taken = 1.8400000000001748e-05
    Ans = True, Time taken = 2.970000000000056e-05     
    Ans = True, Time taken = 5.9700000000002806e-05    
    Ans = False, Time taken = 8.84999999999983e-05'''
    def is_happy(self, n: int) -> bool:
        slow, fast = n, self.squared_sum_of_digits(n)
        print(slow, fast)

        while slow != fast:
            fast = self.squared_sum_of_digits(fast)
            print(fast)
            fast = self.squared_sum_of_digits(fast)
            print(fast)
            slow = self.squared_sum_of_digits(slow)

        return True if fast == 1 else False

    def squared_sum_of_digits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
    
class soln3:
    '''Runtime: 61 ms, faster than 34.10% of Python3 online submissions for Happy Number.
    Memory Usage: 13.9 MB, less than 14.36% of Python3 online submissions for Happy Number.
    Ans = True, Time taken = 1.8400000000001748e-05
    Ans = True, Time taken = 2.970000000000056e-05     
    Ans = True, Time taken = 5.9700000000002806e-05    
    Ans = False, Time taken = 8.84999999999983e-05'''
    def is_happy(self, n: int) -> bool:
        slow, fast = n, sum([int(x) ** 2 for x in str(n)])

        while slow != fast:
            fast = sum([int(x) ** 2 for x in str(fast)])
            fast = sum([int(x) ** 2 for x in str(fast)])
            slow = sum([int(x) ** 2 for x in str(slow)])

        return True if fast == 1 else False
            
test = soln2()

start_time = time.perf_counter()
ans = test.is_happy(82)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.is_happy(7)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.is_happy(19)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.is_happy(11)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

