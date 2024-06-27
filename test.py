from collections import defaultdict

class BaguaghostLeg:
    def __init__(self):
        self.horizontal_lines = defaultdict(dict)

    def add_line(self, i, j, x):
        self.horizontal_lines[x][i] = j
        self.horizontal_lines[x][j] = i

    def dfs(self, current_node, visited, results, code_map):
        visited.add(current_node)
        results.append(code_map[current_node])  # Add current node result

        # Get the edges sorted by the specified order ('r', 's', 't', 'u', 'v')
        edges = sorted(self.horizontal_lines.keys())
        for edge in edges:
            if current_node in self.horizontal_lines[edge]:
                next_node = self.horizontal_lines[edge][current_node]
                if next_node not in visited:
                    self.dfs(next_node, visited, results, code_map)

    def get_results(self):
        results = []
        code_map = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
        visited = set()

        # Perform DFS from each starting node (1 to 8)
        for start_node in range(1, 9):
            if start_node not in visited:
                self.dfs(start_node, visited, results, code_map)

        return results

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    bg_leg = BaguaghostLeg()
    for line in lines:
        if line.strip():
            i, j, x = line.strip().split(',')
            bg_leg.add_line(int(i), int(j), x.strip())
    return bg_leg

def main():
    input_file = 'input.txt'
    bg_leg = read_input(input_file)
    results = bg_leg.get_results()
    for i, result in enumerate(results, start=1):
        print(f"No. {i} 參賽者之籤碼為[{result}]")

if __name__ == "__main__":
    main()
