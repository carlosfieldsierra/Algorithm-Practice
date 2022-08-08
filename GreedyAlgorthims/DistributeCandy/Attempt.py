



def solve(A):
    A.sort()
        
        
    numCandiesToGive = 1
    candies = 1
    prevRating = A[0]
    
    for rating in A[1:len(A)]:
        if rating > prevRating:
            numCandiesToGive += 1
        elif rating < prevRating:
            numCandiesToGive = max(1,numCandiesToGive-1)

        prevRating = rating
        candies+=numCandiesToGive
        
    return candies



def Main():
    
    A = [1,5,2,1]

    ans = solve(A)
    
    print(ans)

if __name__ == "__main__":
    Main()