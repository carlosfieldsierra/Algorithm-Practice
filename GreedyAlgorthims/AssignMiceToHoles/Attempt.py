'''
There are N Mice and N holes that are placed in a straight line. Each hole can accomodate only 1 mouse.
The positions of Mice are denoted by array A and the position of holes are denoted by array B.
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.

Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
'''


def solve(A,B):
    
    distance = []
    for mice in A:
        for hole in B:
            distance.append((
                mice,hole,abs(mice - hole)
            ))
    
    distance.sort(key=lambda x: x[2], reverse=True)


    vistedHole = set()
    vistedMice = set()
    
    nextMice,nextHole,nextDist = getNextMice(distance,vistedMice,vistedHole)
    

def getNextMice(distance,vistedMice,vistedHole):
    
    nonVistedMice = [(mice,hole,dist) for mice,hole,dist in distance \
        if mice not in vistedMice and hole not in vistedHole
        ]

    print(nonVistedMice)


def Main():
    A = [-4, 2, 3]
    B = [0, -2, 4]
    ans = solve(A,B)
    print(ans)

if __name__ == "__main__":
    Main()