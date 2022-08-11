


def solve(A):
    times = {}
    for elem in A:
        if elem not in times:
            times[elem] = 0
        times[elem] +=1
        
    timesLst = [(num,count) for num,count in times.items()]
    timesLst.sort(key=lambda x: x[1])
    return timesLst[-1][0]

def Main():
    ans = solve([2, 1, 2])

    print(f"Answer: {ans}")


if __name__ == "__main__":
    Main()