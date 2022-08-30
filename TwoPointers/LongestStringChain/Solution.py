# Graph Theory Solution
class Solution:
    def longestStrChain(self, words):
        s = set(words)
        memo = {}

        def rec(word):
            if word not in set: return 0
            
            if word in memo:
                return memo[word]
            else:
                N = len(word)
                mx = 0
                for i in range(N):
                    mx(mx,rec(word[:1]+word[i+1:]) + 1)
                memo[word] = mx

            return mx
        words.sort(key=lambda x:len(x),reversed=True)
        for w in words:
            rec(w)
        


        return max(memo.values)