import time
import os
class Smart_Rover:
    def __init__(self , name , map , current_position = (0, 0)):
        self.name = name
        self.current_position = current_position
        self.map = map
        self.previous_positions = []
        self.successfull_routes = []

    def move(self):
        if  len(self.successfull_routes) > 0:
            selected_route = min(self.successfull_routes, key=len)
            self.previous_positions.append(self.current_position)
            self.current_position = selected_route[0]
            self.successfull_routes = [] 


    def memory(self):
        self.explored_positions = []
        last_pos = self.previous_positions[-1] if len(self.previous_positions) > 0 else None
        current_spys = [{"position" : self.current_position , "step" : 0 , "previous_position" : last_pos , "path" : []}]
        while current_spys:
            current_spy = current_spys.pop(0)
            current_position = current_spy["position"]
            current_step = current_spy["step"]
            previous_position = current_spy["previous_position"]
            current_path = current_spy["path"]
            if self.map[current_position[0]][current_position[1]] == 2:
                self.successfull_routes.append(current_path)
                continue
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_position = (current_position[0] + dx, current_position[1] + dy)
                if 0 <= new_position[0] < len(self.map) and 0 <= new_position[1] < len(self.map[0]):
                    is_passable = (self.map[new_position[0]][new_position[1]] == 0) or (self.map[new_position[0]][new_position[1]] == 2)
                    if is_passable:
                        if new_position not in self.previous_positions and new_position not in current_path and new_position != self.current_position and new_position not in self.explored_positions:
                            new_path = current_path + [new_position]
                            current_spys.append({"position": new_position, "step": current_step + 1, "previous_position": current_spy["position"], "path": new_path})
                            self.explored_positions.append(new_position)


import random

def generate_hardcore_map(height=40, width=80):
    # Yükseklik (satır) ve genişlik (sütun) olarak haritayı oluştur
    city = [[0 for _ in range(width)] for _ in range(height)]
    
    # %35 ihtimalle engeller (1) at
    for r in range(height):
        for c in range(width):
            if random.random() < 0.35:
                city[r][c] = 1
                
    # Garanti yol kazısı (Hedefe kesin ulaşım)
    curr_r, curr_c = 0, 0
    while (curr_r, curr_c) != (height-1, width-1):
        city[curr_r][curr_c] = 0
        if curr_r < height-1 and curr_c < width-1:
            if random.random() < 0.5: curr_r += 1
            else: curr_c += 1
        elif curr_r < height-1: curr_r += 1
        elif curr_c < width-1: curr_c += 1
    
    # Başlangıç ve Bitiş
    city[0][0] = 0
    city[height-1][width-1] = 2
    return city

# Monitöründe en kare duracak oranı bulana kadar bu sayıları değiştirebilirsin:
# Örneğin: Yükseklik 40, Genişlik 80
map = generate_hardcore_map(height=40, width=80)

my_rover = Smart_Rover(name= "Smart Rover", map=map, current_position=(0, 0))

print("Rover is starting at position " + str(my_rover.current_position))
time.sleep(2)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if map[my_rover.current_position[0]][my_rover.current_position[1]] == 2:
        print("\n🏆 GÖREV TAMAMLANDI! HEDEFE ULAŞILDI! 🏆")
        break
    my_rover.memory()
    my_rover.move()
    for r in range(len(map)):
        looking_of_row = ""
        for c in range(len(map[0])):
            if (r, c) == my_rover.current_position:
                    looking_of_row += "🤖"
            elif map[r][c] == 2:        
                    looking_of_row += "🎯"       
            elif (r,c) in my_rover.previous_positions:
                    looking_of_row += "👣"
            elif map[r][c] == 1:
                    looking_of_row += "⬛"
            else:
                    looking_of_row += "⬜"
        print(looking_of_row)
    print("STATUS: Rover is at position " + str(my_rover.current_position))
    time.sleep(0.4)

