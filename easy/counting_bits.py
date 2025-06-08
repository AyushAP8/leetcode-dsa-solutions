import time

'''Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''

class soln1:
    '''Runtime: 211 ms, faster than 23.58% of Python3 online submissions for Counting Bits.
    Memory Usage: 20.8 MB, less than 78.97% of Python3 online submissions for Counting Bits.
    Ans = [0, 1, 1], Time taken = 6.600000000002437e-06
    Ans = [0, 1, 1, 2, 1, 2], Time taken = 7.199999999998874e-06'''
    def hamming_wt(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
    
    def counting_bits(self, n: int) -> list[int]:
        ans = []
        cnt = 0
        while cnt <= n:
            ans.append(self.hamming_wt(cnt))
            cnt += 1
        return ans


class soln2:
    '''Runtime: 101 ms, faster than 83.69% of Python3 online submissions for Counting Bits.
    Memory Usage: 20.7 MB, less than 78.97% of Python3 online submissions for Counting Bits.
    Ans = [0, 1, 1], Time taken = 6.499999999992623e-06
     Ans = [0, 1, 1, 2, 1, 2], Time taken = 1.4100000000002999e-05'''
    def counting_bits(self, n: int) -> list[int]:
        bits = [0]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            bits.append(1 + bits[i - offset])
        return bits
    
class soln3:
    ''''''
    def counting_bits(self, n: int) -> list[int]:
        ans = []
        for i in range(n):
            count = 0
            no = bin(n)
            while n:
                count += no % 2
                no /= 2
            ans.append(count)
        return ans
    
    
test = soln3()


start_time = time.perf_counter()
ans = test.counting_bits(2)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
ans = test.counting_bits(5)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")
