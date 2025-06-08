import time

"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

#O(N)
class soln1:
    '''Runtime: 82 ms, faster than 39.52% of Python3 online submissions for Valid Palindrome.
        Memory Usage: 15.1 MB, less than 29.22% of Python3 online submissions for Valid Palindrome.'''
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        ptr1 = 0
        ptr2 = len(s)-1
        if ptr1 == ptr2:
            return True
        while ptr1 < ptr2:
            if s[ptr1] == s[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else:
                return False
        return True
        
#O(N)
class soln2:
    '''Runtime: 106 ms, faster than 16.16% of Python3 online submissions for Valid Palindrome.
    Memory Usage: 14.4 MB, less than 57.28% of Python3 online submissions for Valid Palindrome.'''
    def isalphanumeric(self, char: str) -> bool:
        return((ord('A')<=ord(char)<=ord('Z')) or
               (ord('a')<=ord(char)<=ord('z')) or
               (ord('0')<=ord(char)<=ord('9')))
               
    def is_palindrome(self, s: str) -> bool:
        lptr, rptr = 0, len(s) - 1
        while lptr < rptr:
            while lptr < rptr and not self.isalphanumeric(s[lptr]):
                lptr += 1
            while lptr < rptr and not self.isalphanumeric(s[rptr]):
                rptr -= 1
            if s[lptr].lower() != s[rptr].lower():
                return False
            lptr += 1
            rptr -= 1
        return True
                               
                

test = soln2()

start = time.perf_counter()
mp = test.is_palindrome("A man, a plan, a canal Panama")
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")

start = time.perf_counter()
mp = test.is_palindrome("race a car")
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")

start = time.perf_counter()
mp = test.is_palindrome(" ")
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")


