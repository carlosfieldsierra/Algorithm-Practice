'''
    Given an 2D integer array A of size N x 2 
    denoting time intervals of different meetings.

    Where:

    

    A[i][0] = start time of the ith meeting.
    A[i][1] = end time of the ith meeting.
    

    Find the minimum number of conference rooms 
    required so that all meetings can be done.

    Note :- If a meeting ends at time t, 
    another meeting starting at time t can use the same 
    conference room
'''
'''       
            -- -   11--16
        5 ---- 10  15 --------------35
    0 ------------------ 30 33 ------------ 50
'''


# O(N*LOG(N)) runtime | O(N*2) spacetime
def solve(A):
    # Number of meetings for a confrence room
    curr = 0
    # Number of confernce rooms
    curMax  = 0

    
    sortedTimes = [
        f(meeting) for meeting in A for f \
             in (lambda x: (x[0],1),lambda x: (x[1],-1))]

    sortedTimes.sort(key=lambda x: x[0])

    for _,e in sortedTimes:
        curr += e
        curMax = max(curr,curMax)

    return curMax




    


def Main():
    A = [
        [7,   10],
        [4,   19],
        [19,  26],
        [14,  16],
        [13,  18],
        [16,  21],
    ]

    ans = solve(A)

    print(ans)


if __name__ == "__main__":
    Main()