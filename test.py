from collections import defaultdict

class BaguaGhostLeg:
    def __init__(self):
        self.horizontal_lines = defaultdict(dict)

    def add_line(self, i, j, x):
        self.horizontal_lines[x][i] = j
        self.horizontal_lines[x][j] = i

    def dfs(self, current_pos, visited):
        visited.add(current_pos)
        for x in ['r', 's', 't', 'u', 'v']:
            if current_pos in self.horizontal_lines[x]:
                next_pos = self.horizontal_lines[x][current_pos]
                if next_pos not in visited:
                    return self.dfs(next_pos, visited)
        return current_pos

    def get_final_position(self, start):
        visited = set()
        final_pos = self.dfs(start, visited)
        return final_pos

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    bg_leg = BaguaGhostLeg()
    for line in lines:
        if line.strip():
            i, j, x = line.strip().split(',')
            bg_leg.add_line(int(i), int(j), x.strip())
    return bg_leg

def main():
    input_file = 'input.txt'
    bg_leg = read_input(input_file)
    results = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for i in range(1, 9):
        final_pos = bg_leg.get_final_position(i)
        print(f"No. {i} 參賽者之籤碼為[{results[final_pos-1]}]")

if __name__ == "__main__":
    main()
