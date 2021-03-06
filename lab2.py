#!/usr/bin/env python
# coding: utf-8

# In[ ]:


open = ["[", "{", "("]
close = ["]", "}", ")"]

def check(Str):
    stack = []
    for i in Str:
        if i in open:
            stack.append(i)
        elif i in close:
            pos = close.index(i)
            if ((len(stack) > 0) and
                    (open[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
        
string = "{[]{()}}"
print(string, "-", check(string))
string = "[{}{})(]"
print(string, "-", check(string))
string = "((()"
print(string, "-", check(string))

