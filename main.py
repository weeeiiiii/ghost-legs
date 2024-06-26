import sys

outcomes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

horizontal_edges = {}

def initialize_horizontal_edges(filename):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            i = int(parts[0])
            j = int(parts[1])
            x = parts[2].strip()

            horizontal_edges[f"{i}_{j}_{x}"] = (i - 1, j - 1, x)

def traverse(start_axis):
    current_axis = start_axis - 1
    branches = ['r', 's', 't', 'u', 'v']
    current_branch = 0

    while current_branch < len(branches):
        moved = False
        for i in [-1, 1]:
            next_axis = (current_axis + i + 8) % 8
            edge_key = f"{current_axis + 1}_{next_axis + 1}_{branches[current_branch]}"
            if edge_key in horizontal_edges:
                current_axis = next_axis
                moved = True
                break
        if not moved:
            current_branch += 1
    
    return outcomes[current_axis]


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py input.txt")
        return

    filename = sys.argv[1]
    initialize_horizontal_edges(filename)

    for i in range(1, 9):  
        result = traverse(i)
        print(f"No. {i} 參賽者之籤碼為[ {result} ]")

if __name__ == "__main__":
    main()
