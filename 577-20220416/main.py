"""
Problem description
Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.
For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following circle: chair --> racket --> touch --> height --> tunic --> chair.
"""

l1 = ['chair', 'height', 'racket', 'touch', 'tunic']
l2 = ['chair', 'height', 'racket', 'tunic']

# Recursive method to check the circularity of the list
def check_list(l, old=[0], start=0):
    # If 'old' has the same length as 'l', then we have already checked the entire circularity
    if len(old) == len(l):
        return True
    else:
        item = l[start]
        available = []
        # Search for possible next items
        for j in range(0, len(l)):
            if (start != j) and (l[j][0] == item[-1]) and (j not in old):
                available.append(j)
        # Investigate circularity on possible next items 
        for z in available:
            old.append(z)
            r = check_list(l, old, start=z)
            if r:
                return True
        # If no future branches, then list is not circular
        return False

if __name__ == '__main__':
    l_all = [l1, l2]
    for l in l_all:
        flag = False
        for i in range(0, len(l)):
            r = check_list(l, old=[i], start=i)
            print(f'List {l} is circular starting from {i}? {r}')
            if r:
                break