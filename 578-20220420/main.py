"""
Problem description
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

s1 = "abc"
s2 = "bcd"
s3 = "foo"
s4 = "bar"

def check_strings(a, b):
    d = {}
    for i in range(0, len(a)):
        if a[i] not in d:
            d[a[i]] = b[i]
        if d[a[i]] != b[i]:
            return False
    return True
  
print(f'String "{s1}" and "{s2}" can be mapped correctly? {check_strings(s1, s2)}')
print(f'String "{s3}" and "{s4}" can be mapped correctly? {check_strings(s3, s4)}')
