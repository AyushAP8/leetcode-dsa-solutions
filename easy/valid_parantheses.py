from itertools import count
import time

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class soln1:
    def valid_parantheses(self, s: str) -> bool:
        history = list()
        index = 0
        for i in s:
            history.append(i)
            if i not in history and history.index(i) == index:
                index += 1
                print(history, index)
            else:
                return False
            return True
        
class soln2:
    def valid_parantheses(self, s: str) -> bool:
        count_dict = dict()
        for i in s:
            print(count_dict)
            count_dict[i] = 1 + count_dict.get(i, 0)
        for i in count_dict.keys():
            if count_dict[i]%2 != 0:
                return False
        return True
    
class soln3:
    def valid_parantheses(self, s: str) -> bool:
        '''Runtime: 60 ms, faster than 21.41% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 13.9 MB, less than 70.03% of Python3 online submissions for Valid Parentheses.'''
        parantheses_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:        
            if c not in parantheses_map:
                stack.append(c)
                continue
            if not bool(stack) or stack[-1] != parantheses_map[c]:
                return False
            stack.pop()
        return not bool(stack)
                
            
        
test = soln3()

start = time.perf_counter()
ans = test.valid_parantheses("[")
end = time.perf_counter()
print(ans)
print(f"time = {end - start}") 

start = time.perf_counter()
ans = test.valid_parantheses("()")
end = time.perf_counter()
print(ans)
print(f"time = {end - start}") 

start = time.perf_counter()
ans = test.valid_parantheses("()[]{}")
end = time.perf_counter()
print(ans)
print(f"time = {end - start}") 

start = time.perf_counter()
ans = test.valid_parantheses("(]")
end = time.perf_counter()
print(ans)
print(f"time = {end - start}")      