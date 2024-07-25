from collections import defaultdict

class BaguaghostLeg:
    def __init__(self):
        self.horizontal_lines = defaultdict(dict)

    def add_line(self, i, j, x):
        self.horizontal_lines[x][i] = j
        self.horizontal_lines[x][j] = i

    def final_position(self, start):
        current_pos = start
        for x in ['v', 'u', 't', 's', 'r']:
            if current_pos in self.horizontal_lines[x]:
                new_pos = self.horizontal_lines[x][current_pos]
                #print(f"Moved from position {current_pos} to {new_pos} via {x}") 
                current_pos = new_pos  
        return current_pos

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    bg_leg = BaguaghostLeg()
    for line in lines:
        if line.strip():
            i, j, x = line.strip().split(',')
            bg_leg.add_line(int(i), int(j), x.strip())
            #print(f"Added line: {i}, {j}, {x.strip()}") 
    return bg_leg

def main():
    input_file = 'input.txt'
    bg_leg = read_input(input_file)
    results = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for i in range(1, 9):
        final_pos = bg_leg.final_position(i)
        print(f"No. {i} 參賽者之籤碼為[{results[final_pos-1]}]")

if __name__ == "__main__":
    main()


