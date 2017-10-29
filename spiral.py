"""
Prints a 'spiraling matrix' of size (n, n) starting at a given corner and moving either clockwise or counterclockwise
e.g. spiral(6, 1, False) returns a matrix size starting with 1 in top right corner, incrementing counterclockwise (left)
here's the output:
 6  5  4  3  2  1
 7 24 23 22 21 20
 8 25 34 33 32 19
 9 26 35 36 31 18
10 27 28 29 30 17
11 12 13 14 15 16

https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/
"""


def spiral(n, corner, clockwise=True):
    matrix = [[0 for i in range(n)] for k in range(n)]  # create empty matrix
    corner_coordinates = {0: (0, 0), 1: (n-1, 0), 2: (n-1, n-1), 3: (0, n-1)}  # define corners
    directions = {'e': (1, 0), 'n': (0, -1), 'w': (-1, 0), 's': (0, 1)}  # define directions
    orientation_order = ['e', 's', 'w', 'n']  # default direction order starting from top left moving clockwise
    x, y = corner_coordinates[corner]
    d = 1
    if not clockwise:
        corner = (corner + 1) % 4
        d = -1
    dx, dy = directions[orientation_order[corner]]
    for num in range(1, (n**2)+1):
        if next_blocked(matrix, y, x, dx, dy, n):
            corner = (corner + d) % 4  # cycle through directions, %4 assures only 0, 1, 2, or 3 can be returned
            dx, dy = directions[orientation_order[corner]]
        matrix[y][x] = str(num).rjust(len(str(n**2)))  # write value to matrix with padding of width n**2
        y += dy
        x += dx
    final = '\n'.join(" ".join(row) for row in matrix)
    return final


def next_blocked(matrix, y, x, dx, dy, n):
    """ tests if next cell has a value, or if edge of matrix has been reached """
    if False in [0 <= x+dx < n, 0 <= y+dy < n]:  # edge reached
        return True
    if matrix[y+dy][x+dx] != 0:  # next value not 0
        return True
    return False


if __name__ == '__main__':
    result = spiral(6, 1, False)
    print(result)
