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


def solve(A):
    # Sort by first value
    A.sort(key=lambda x: x[0])
    # Keep track of meetings assigned
    visted = set() 
    # Confernce rooms
    lst = []
    for i in range(len(A)):
        if i in visted:
            continue
        mergedList = A[i]
        visted.add(i)
        for j in range(len(A)):
            if j in visted:
                continue

            ps, pe = mergedList[0], mergedList[-1]
            cs,ce  = A[j]
            # Check if starts After
            if cs >= pe:
                mergedList = mergedList + A[j]
                # Add to visted
                visted.add(j)
            # Check if starts before
            if ce <= ps:
                mergedList =  A[j] + mergedList
                # Add to visted
                visted.add(j)

        
        lst.append(mergedList)

    

    return len(lst)


def Main():
    A = [
        [7, 10],
        [4, 19],
        [19, 26],
        [14, 16],
        [13, 18],
        [16, 21],
    ]

    ans = solve(A)

    print(ans)

if __name__ == "__main__":
    Main()