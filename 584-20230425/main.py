"""
Problem description - Easy
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.
For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""

def replace_two_chars(s, i, j):
    l = list(s)
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
    s1 = ''.join(l)
    return s1

def rearrange(s):
    for i in range(1, len(s)):
        # if two consecutive chars are equal, then replace the second one with another one
        if s[i] == s[i - 1]:
            flipped = False
            for j in range(i + 1, len(s)):
                if s[i] != s[j]:
                    s = replace_two_chars(s, i, j)
                    flipped = True
                    break
            if not flipped:
                return None
    return s


if __name__ == '__main__':
    s1 = 'aaabbc'
    s2 = 'aaab'
    s = [s1, s2]

    for i in s:
        res = rearrange(i)
        if res:
            print(f'Can string {s} be rearrenged? Yes, {res}')
        else:
            print(f'Can string {s} be rearrenged? No, {res}')