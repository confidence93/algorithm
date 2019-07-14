class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visit = [0]*n 
        out_degree = [0] * n 
        reversed_graph = [[] for x in range(n)] 
        for cur in range(n):
            out_degree[cur] = len(graph[cur])
            for next in graph[cur]:
                reversed_graph[next].append(cur)

        queue = []
        result = []
        for i in range(n): 
            if len(graph[i]) == 0:
                queue.append(i)
        while queue:
            cur = queue.pop(0)
            visit[cur] = 1
            for num in reversed_graph[cur]:
                #my_graph[num].remove(cur)
                out_degree[num] -= 1
                if(out_degree[num] == 0):
                    queue.append(num)
        for i in range(n):
            if(visit[i] == 1):
                result.append(i)
        return (result)
