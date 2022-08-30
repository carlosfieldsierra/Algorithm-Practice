class Solution:
    def compress(self, chars):
        
        prev = None
        index = 0
        count = 1
        while len(chars) > index:

            if chars[index] == prev:
                count += 1
            else:
                if count == 1:
                    pass
                else:
                    newChars = chars[0:index-count] + [chars[index-count]] + [l for l in str(count)]
                    index = len(newChars)  
                    chars = newChars + chars[index+1:]
                    
                count = 1

                
            prev = chars[index]
            index += 1
                
                
        if count > 1:
            chars = chars[0:index-count] + [chars[index-count]] + [l for l in str(count)] + chars[index:]
        
        return len(chars)




def Main():
    ans = Solution().compress(["a","a","b","b","c","c","c"])
    print(f"\nAnswer: {ans}\n")
    ans = Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()