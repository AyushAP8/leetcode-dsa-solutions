import time 

'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Constraints:

The input must be a binary string of length 32.
'''

class soln1:
    def hamming_wt(self, n: int) -> int:
        '''space and time = O(1) but we still have to look all the bits'''
        res = 0
        #traverse through the 32 bits
        while n:
            res += n % 2
            n = n >> 1
        return res
            
    
class soln2:
    def hamming_wt(self, n: int) -> int:
        '''space and time = O(1) - how it works = https://youtu.be/5Km3utixwZs'''
        res = 0
        #traverse through only the 1's
        while n:
            n &= n - 1
            res += 1
        return res
    
test = soln1()

start_time = time.perf_counter()
n = 0o00000000000000000000000000001011
ans = test.hamming_wt(n)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
n = 0o00000000000000000000000010000000
ans = test.hamming_wt(n)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
n = 0o11111111111111111111111111111101
ans = test.hamming_wt(n)
print(f"Ans = {ans}, Time taken = {time.perf_counter() - start_time}")