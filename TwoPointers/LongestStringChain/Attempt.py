# Graph Theory Solution
class Solution:
    def longestStrChain(self, words):
        
        graph = {}
        words.sort(key=lambda x: len(x))
        for word in words:
            length = len(word)
            for i in range(length):
                key = word[0:i] + word[i+1:]
                if key in graph:
                    graph[key].append(word)
            
            graph[word] = []
        
        maxLength = 0
        memo = {}
        for node in graph:
            
            length = maxPath(graph,node,memo) if node not in memo else memo[node]
            maxLength = max(maxLength,length)
            memo[node] = maxLength
            
        return maxLength + 1


def maxPath(graph,node,memo):
    if node in memo:
        return memo[node]
    if graph[node] == []:
        return 0
    maxLength = 0
    for child in graph[node]:
        length = maxPath(graph,child,memo)
        maxLength = max(maxLength,length)
    memo[node] = maxLength
    
    return 1 + maxLength
            