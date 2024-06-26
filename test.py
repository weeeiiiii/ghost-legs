from collections import defaultdict, deque

outcomes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
horizontal_edges = defaultdict(list)

def initialize_horizontal_edges(filename):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            i = int(parts[0])
            j = int(parts[1])
            x = parts[2].strip()
            horizontal_edges[i].append((j, x))
            horizontal_edges[j].append((i, x))

# BFS traversal
def bfs(start):
    visited = set()
    visited.add(start)
    queue = deque([start])
    result = []

    while queue:
        current_axis = queue.popleft()
        result.append(current_axis)

        next_edges = sorted(horizontal_edges[current_axis], key=lambda x: outcomes.index(x[1]))

        for next_axis, branch in next_edges:
            if next_axis not in visited:
                visited.add(next_axis)
                queue.append(next_axis)

    return result

def main():
    filename = "input.txt"
    initialize_horizontal_edges(filename)

    for i in range(1, 9):
        result_order = bfs(i)
        result = outcomes[result_order[-1] - 1]  
        print(f"No. {i} 參賽者支籤碼為[ {result} ]")

if __name__ == "__main__":
    main()
