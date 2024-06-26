from collections import defaultdict

#籤碼
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

# DFS
def dfs(current_axis, current_branch, visited):
    visited.add((current_axis, current_branch))


    next_edges = sorted(horizontal_edges[current_axis], key=lambda x: x[1])
    for next_axis, branch in next_edges:
        if branch > current_branch and (next_axis, branch) not in visited:
            return dfs(next_axis, branch, visited)
    return current_axis

def main():
    filename = "input.txt" 
    initialize_horizontal_edges(filename)

    for i in range(1, 9):
        visited = set()
        result_axis = dfs(i, 'r', visited) 
        result = outcomes[result_axis - 1]
        print(f"No. {i} 参賽者之籤碼為[ {result} ]")

if __name__ == "__main__":
    main()
