from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited, path):
        visited.add(v)
        path.append(v)
        
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, path)
    
    def DFS(self, v):
        visited = set()
        path = []
        self.DFSUtil(v, visited, path)
        return path

def build_bagua_graph(filename):
    g = Graph()
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # 忽略空行
                parts = line.split(', ')
                if len(parts) == 3:  # 确保有3个值
                    i, j, x = parts
                    i, j = int(i), int(j)
                    g.addEdge((i, x), (j, x))
                    g.addEdge((j, x), (i, x))
    return g

if __name__ == "__main__":
    filename = 'input.txt'
    g = build_bagua_graph(filename)
    
    start_points = [(i, 'Pr') for i in range(1, 9)]
    outcomes = ['F', 'A', 'D', 'H', 'E', 'B', 'G', 'C']
    
    results = []
    for i, start in enumerate(start_points):
        path = g.DFS(start)
        final_pos = path[-1][0]
        result = f"No. {i + 1} 參賽者之籤碼為[ {outcomes[final_pos - 1]} ]"
        results.append(result)
    
    for result in results:
        print(result)
