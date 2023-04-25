"""
Problem description - Easy
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and
{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""

r1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
r2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

def point_is_in(x, y, rectangle):
    if x > rectangle['top_left'][0] and x < (rectangle['top_left'][0] + rectangle['dimensions'][0]):
        if y < rectangle['top_left'][1] and y > (rectangle['top_left'][1] - rectangle['dimensions'][1]):
            print(f'({x},{y}),{rectangle} -- INTERSECT')
            return 1
    print(f'({x},{y}),{rectangle} -- NO INTERSECT')
    return 0

def intersection(r1, r2):
    # count how many points in r1 overlaps in r2
    sum = 0
    for x in range(0, r1['dimensions'][0]):
        for y in range(0, r1['dimensions'][1]):
            sum = sum + point_is_in(
                r1['top_left'][0] + x,
                r1['top_left'][1] - y,
                r2
            )
    return sum

if __name__ == '__main__':  
    print(f'Total Intersection {intersection(r1, r2)}')