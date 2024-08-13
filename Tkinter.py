import tkinter as tk
from tkinter import messagebox
from collections import defaultdict

class BaguaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("八卦鬼腳圖抽籤盤")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(3, weight=1) 
        self.file_path = 'input.txt'  
        self.create_widgets()

    def create_widgets(self):
        self.label_edges = tk.Label(self.root, text="邊數:")
        self.label_edges.grid(row=0, column=0) 
        self.entry_edges = tk.Entry(self.root)
        self.entry_edges.grid(row=0, column=1, sticky="EW")  

        self.label_participants = tk.Label(self.root, text="參賽者數量:")
        self.label_participants.grid(row=1, column=0)
        self.entry_participants = tk.Entry(self.root)
        self.entry_participants.grid(row=1, column=1, sticky="EW")  

        self.btn_run = tk.Button(self.root, text="GO", command=self.run_program)
        self.btn_run.grid(row=2, column=0, columnspan=2) 

        self.text_output = tk.Text(self.root, font=("Arial", 18), height=15, width=40)
        self.text_output.tag_configure("center", justify='center')
        self.text_output.grid(row=3, column=0, columnspan=2, sticky="NSEW")

    def run_program(self):
        try:
            num_edges = int(self.entry_edges.get())
            num_participants = int(self.entry_participants.get())

            if num_participants > num_edges:
                messagebox.showerror("錯誤", f"超出參賽者數量，目前最多{num_edges}個參賽者。")
                return 

            bg_leg = read_input(self.file_path, num_edges, num_participants)
            results = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][:num_participants]

            self.text_output.delete(1.0, tk.END) 
            
            for i in range(1, num_participants + 1):
                final_pos = bg_leg.final_position(i)
                if 1 <= final_pos <= num_participants:
                    self.text_output.insert(tk.END, f"No. {i} 參賽者之籤碼為[{results[final_pos-1]}]\n","center")
                else:
                    self.text_output.insert(tk.END, f"No. {i} 參賽者之籤碼為[無效位置]\n","center")
        except ValueError:
            messagebox.showerror("請輸入有效的數值！")

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
        for x in ['v', 'u', 't', 's', 'r']:
            if current_pos in self.horizontal_lines[x]:
                new_pos = self.horizontal_lines[x][current_pos]
                if new_pos < 1 or new_pos > self.num_participants:
                    return -1
                current_pos = new_pos
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

if __name__ == "__main__":
    root = tk.Tk()
    app = BaguaApp(root)
    root.mainloop()
