

def solve(A):
    n = len(A)
    ans = 0
    for b in range(32):
        ones = 0
        for num in A:
            if (1 << b) & num:
                ones += 1
        if ones > n // 2:
            ans += (1 << b)

def Main():
    ans = solve([2,1,2])
    print(f"Answer: {ans}")
