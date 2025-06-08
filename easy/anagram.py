import time

"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
#O(N)
class soln1:
    def anagram(self, s: str, t: str) -> bool:   
        '''Runtime: 98 ms, faster than 21.72% of Python3 online submissions for Valid Anagram.
        Memory Usage: 14.5 MB, less than 66.69% of Python3 online submissions for Valid Anagram.'''    
        if len(s) != len(t):
            return False
        
        def str_to_dict(s: str) -> dict:
            hmap = dict()
            for i in s:
                if i in hmap.keys():
                    hmap[i] += 1 
                else:
                    hmap[i] = 0
            return hmap
        print(str_to_dict(s), str_to_dict(t))
        return str_to_dict(s) == str_to_dict(t)

#O(N    )    
class soln2:
    '''Runtime: 77 ms, faster than 50.19% of Python3 online submissions for Valid Anagram.
    Memory Usage: 14.4 MB, less than 96.92% of Python3 online submissions for Valid Anagram.'''
    def anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap_s = dict()
        hmap_t = dict()
        for i in range(len(s)):
            hmap_s[s[i]] = 1 + hmap_s.get(s[i], 0)
            hmap_t[t[i]] = 1 + hmap_t.get(t[i], 0)
        return  hmap_t == hmap_s
    
                

test = soln2()

start = time.perf_counter()
mp = test.anagram('anagram', 'nagaram')
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")

start = time.perf_counter()
mp = test.anagram('anagram', 'dfnagaram')
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")

start = time.perf_counter()
mp = test.anagram('cat', 'bat')
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")

start = time.perf_counter()
mp = test.anagram('aacc', 'ccac')
end = time.perf_counter()
print(mp)
print(f"time = {end - start}")