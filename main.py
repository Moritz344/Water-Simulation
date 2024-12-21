import pygame
import random

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Water Simulation")
clock = pygame.time.Clock()

rows = 50
cols = 50
cell_size = 20
num_water = 0

def spawn_grid():
    for row in range(rows):
        for col in range(cols):

            x = row * cell_size
            y = col * cell_size

            pygame.draw.rect(screen,"black",(x,y,cell_size,cell_size),1)


class Water(object):
    def __init__(self,nums,x,y,):
        self.water_block = 20
        self.num = nums
        self.x = x
        self.y = y
        self.water_dx = -1
        self.water_dy = -1
        self.water_x_speed = 1
        self.water_y_speed = 5


        #for i,v in enumerate(water):
            #print(f"Water Block:{i+1}: {v}")

    def update(self):
        for row,col in water:
            self.water = pygame.draw.rect(screen,(25, 123, 189),(row * cell_size,col * cell_size,cell_size,cell_size))
            self.waterRect = pygame.Rect(row * cell_size,col * cell_size,cell_size,cell_size)
        
        # beim gedrückt halten spawnen
        mouse_button = pygame.mouse.get_pressed()
        if mouse_button[0]:
            self.erzeugeWater()
        elif mouse_button[2]:
            self.del_water()


    def WaterMovement(self):
        global water,num_water
        updated_water = water.copy()
        
        for x,y in sorted(water,reverse=True):
            if (x, y + 1) not in updated_water and y + 1 <= cols-21:
                if (x,y ) in updated_water:
                    updated_water.remove((x, y))
                updated_water.append((x, y + 1))

        water = updated_water

    def erzeugeWater(self):
        global num_water
        mouse_x,mouse_y = pygame.mouse.get_pos()

        self.x= mouse_x // cell_size
        self.y= mouse_y // cell_size
        water.append((self.x,self.y))
        # print(f"water placed at {self.x,self.y}")

    def del_water(self):
        global num_water
        mouse_x,mouse_y = pygame.mouse.get_pos()

        self.x = mouse_x // cell_size
        self.y = mouse_y // cell_size
        try:
            water.remove((self.x,self.y))
            print(f"water removed at {self.x,self.y}")
        except Exception:
            print(f"I can't find water to remove at {self.x,self.y}")

water = [[random.randint(0,rows) ,random.randint(0,cols)  ] for _ in range(num_water)]
w: object = Water(0,0,2)

run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run: bool = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run: bool = False


    screen.fill("white")
    spawn_grid()
    
    w.update()
    w.WaterMovement()
    pygame.display.update()
    clock.tick(60)


