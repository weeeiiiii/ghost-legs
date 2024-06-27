class BaguaghostLeg:
    def __init__(self):
        self.horizontal_lines = {}

    def add_line(self, i, j, x):
        if x not in self.horizontal_lines:
            self.horizontal_lines[x] = {}
        self.horizontal_lines[x][(i, j)] = True
        self.horizontal_lines[x][(j, i)] = True

    def get_final_position(self, start):
        current_pos = start
        for x in ['r', 's', 't', 'u', 'v']:
            if x in self.horizontal_lines:
                if (current_pos, current_pos % 8 + 1) in self.horizontal_lines[x]:
                    current_pos = current_pos % 8 + 1
                elif (current_pos, (current_pos - 2) % 8 + 1) in self.horizontal_lines[x]:
                    current_pos = (current_pos - 2) % 8 + 1
        return current_pos

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
    results = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for i in range(1, 9):
        final_pos = bg_leg.get_final_position(i)
        print(f"No. {i} 參賽者之籤碼為[{results[final_pos - 1]}]")

if __name__ == "__main__":
    main()
