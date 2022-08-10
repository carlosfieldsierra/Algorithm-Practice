'''
There are N Mice and N holes that are placed in a straight line. Each hole can accomodate only 1 mouse.
The positions of Mice are denoted by array A and the position of holes are denoted by array B.
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.

Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
'''


def solve(A,B):
    A.sort()
    B.sort()
    return max([abs(mice-hole) for mice,hole in zip(A,B)])

def Main():
    A = [-4, 2, 3]
    B = [0, -2, 4]
    ans = solve(A,B)
    print(f"Answer: {ans}")


if __name__ == "__main__":
    Main()