


def solve(arr,target):
    N = len(arr)
    mod = 10**9 + 7
    counterMap = {}
    for value in arr:
        if value not in counterMap:
            counterMap[value] = 0
        counterMap[value]+=1
    output = 0
    keys = sorted(counterMap)
    for i,num1 in enumerate(keys):
        j, k = i, N - 1
        T = target - num1
        while j <= k: 
            num2, num3 = keys[j],keys[k]
            if num2 + num3 < T:
                j += 1
            elif num2 + num3 > T:
                k -= 1
            else:
                if i < j < k:
                    output += counterMap[num1] + counterMap[num2] + counterMap[num3]
                if i==j<k:
                    output += counterMap[num1] + counterMap[num2] + counterMap[num3]

    return 
 
def Main():
    ans = solve(arr = [1,1,2,2,3,3,4,4,5,5], target = 8)
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()