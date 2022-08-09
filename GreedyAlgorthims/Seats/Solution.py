'''
    There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.
    An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
    Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.
    Return minimum value % MOD where MOD = 10000003
'''



def solve(A):
    MOD = 10000003

    # All the indices of xs
    crosses = [index for index, elem in enumerate(A) if elem == 'x']
    # moves them all to start at the posion 0
    # not nessicarly the first index of the array
    # but the first index in the list
    print(crosses)
    crosses = [(cross-index) for index,cross in enumerate(crosses)]
    print(crosses)
    # Edge case
    length = len(crosses)
    if length == 0: return 0

    ans = float('inf')


    for segment_start in range(len(A)):
        total = 0
        for cross in crosses:
            total += abs(cross - segment_start)
            total %= MOD
        ans = min(ans, total % MOD)



    return ans

def Main():
    A = "....x..xx...x.."
    ans = solve(A) 
    print(ans)


if __name__ == "__main__":
    Main()