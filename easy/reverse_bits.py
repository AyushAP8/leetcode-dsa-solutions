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
    def reverse_bits(self, n: int) -> int:
        return bin(2147483647 - int(n))    
    
class soln2:
    '''Runtime: 41 ms, faster than 78.25% of Python3 online submissions for Reverse Bits.
    Memory Usage: 13.9 MB, less than 7.67% of Python3 online submissions for Reverse Bits.
    Ans = 0b10010000010000000000000000000000, Time taken = 8.600000000004437e-06
    Ans = 0b10000000000, Time taken = 3.639999999999893e-05
    Ans = 0b10000010010010010010010010010010, Time taken = 1.7200000000001936e-05
    Ans = 0b100000000000000000000000000000, Time taken = 1.9299999999999873e-05'''
    def reverse_bits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res     
    
    
test = soln2()

start_time = time.perf_counter()
n = 0o00000000000000000000000000001011
ans = test.reverse_bits(n)
print(f"Ans = {bin(ans)}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
n = 0o00000000000000000000000010000000
ans = test.reverse_bits(n)
print(f"Ans = {bin(ans)}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
n = 0o11111111111111111111111111111101
ans = test.reverse_bits(n)
print(f"Ans = {bin(ans)}, Time taken = {time.perf_counter() - start_time}")

start_time = time.perf_counter()
n = 0b100
ans = test.reverse_bits(n)
print(f"Ans = {bin(ans)}, Time taken = {time.perf_counter() - start_time}")