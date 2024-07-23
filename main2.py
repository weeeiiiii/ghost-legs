from collections import defaultdict

class BaguaghostLeg:
    def __init__(self, num_edges, num_participants):
        self.horizontal_lines = defaultdict(dict)
        self.num_edges = num_edges
        self.num_participants = num_participants

    def add_line(self, i, j, x):
        if 1 <= i <= self.num_participants and 1 <= j <= self.num_participants:
            self.horizontal_lines[x][i] = j
            self.horizontal_lines[x][j] = i
        else:
            print(f"無效的水平連接: {i}, {j}, {x}")

    def final_position(self, start):
        current_pos = start
        print(f"開始於位置: {current_pos}")  
        for x in ['v', 'u', 't', 's', 'r']:
            if current_pos in self.horizontal_lines[x]:
                new_pos = self.horizontal_lines[x][current_pos]
                print(f"從位置 {current_pos} 經過 {x} 移動到位置 {new_pos}")  
                if new_pos < 1 or new_pos > self.num_participants:
                    print(f"位置 {new_pos} 超出有效範圍")
                    return -1
                current_pos = new_pos
        print(f"最終位置: {current_pos}")  
        return current_pos

def read_input(file_path, num_edges, num_participants):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    bg_leg = BaguaghostLeg(num_edges, num_participants)
    for line in lines:
        if line.strip():
            i, j, x = line.strip().split(',')
            bg_leg.add_line(int(i), int(j), x.strip())
    return bg_leg

def main():
    input_file = 'input.txt'
    num_edges = int(input("請輸入邊數: "))
    num_participants = int(input("請輸入參賽者數量: "))
    
    bg_leg = read_input(input_file, num_edges, num_participants)
    
    results = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][:num_participants]  
    for i in range(1, num_participants + 1):
        final_pos = bg_leg.final_position(i)
        if 1 <= final_pos <= num_participants:
            # TODO IndexError: list index out of range
            print(f"No. {i} 參賽者之籤碼為[{results[final_pos-1]}]")
        else:
            print(f"No. {i} 參賽者之籤碼為[無效位置]")

if __name__ == "__main__":
    main()
