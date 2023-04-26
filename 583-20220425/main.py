"""
Problem description - Medium
You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""

matrix = [
    [0, 3, 1, 1], 
    [2, 0, 0, 4],
    [1, 5, 3, 1]
]

def collect_coins(m, i=0, j=0, p=[]):
    # find the maximum number of coins you can find

    # define base variables
    p2 = [m[i][j]]
    p3 = []
    sum_x = 0
    sum_y = 0

    # navigate the entire matrix space collecting the sum of elements and followed path
    if i < len(m) and j < len(m[i]) - 1:
        (sum_x, p3) = collect_coins(m, i, j + 1, p2)
    if i < len(m) - 1 and j < len(m[i]):
        (sum_y, p3) = collect_coins(m, i + 1, j, p2)

    # extract value of this point
    sum = m[i][j]
    # select the best branch followed and add to it the value of the actual cell
    if sum_x > sum_y:
        sum = sum + sum_x
    else:
        sum = sum + sum_y

    # return best result up to now
    return sum, p2 + p3

if __name__ == '__main__':  
    print(f'Maximum collection {collect_coins(matrix)}')