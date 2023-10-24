# Example file showing a circle moving on screen
# pylint: disable=no-member
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()

# โหลดรูปภาพพื้นหลัง
# โหลดรูปภาพพื้นหลังแบบรวมทั้งหมดเข้าด้วยกัน
background_combined = pygame.image.load('static/image/graveyardtilesetnew/png/BG_combined-1.png').convert()
# ตำแหน่ง X ของรูปภาพพื้นหลัง
background_x = -2000

# โหลดรูปภาพวัตถุ
floor_image = pygame.image.load('static/image/graveyardtilesetnew/png/Tiles/Tile (2).png').convert()
floor_width = floor_image.get_width()


class Player:
    def __init__(self, x, y, width, height):
        self.speed = 0.1
        self.x = x
        self.y = y
        self.animation_frames = [
            pygame.image.load('static/image/jackfree/png/Walk (1).png'),
            pygame.image.load('static/image/jackfree/png/Walk (2).png'),
            pygame.image.load('static/image/jackfree/png/Walk (3).png'),
            pygame.image.load('static/image/jackfree/png/Walk (4).png'),
            pygame.image.load('static/image/jackfree/png/Walk (5).png'),
            pygame.image.load('static/image/jackfree/png/Walk (6).png'),
            pygame.image.load('static/image/jackfree/png/Walk (7).png'),
            pygame.image.load('static/image/jackfree/png/Walk (8).png'),
            pygame.image.load('static/image/jackfree/png/Walk (9).png'),
            pygame.image.load('static/image/jackfree/png/Walk (10).png'),
            # เพิ่มรูปภาพเฟรมอื่น ๆ ตรงนี้
        ]
        self.animation_frames = [pygame.transform.scale(frame, (width, height)) for frame in self.animation_frames]

         
        # ตำแหน่งเริ่มต้นของ animation
        self.animation_frame = 0
        self.frame_rate = 10  # อัตราเฟรมต่อวินาที
        self.frame_delay = 1000 / self.frame_rate  # คำนวณเวลาที่ต้องรอระหว่างเฟรม
       
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    # เพิ่มเมทอด move_right() เพื่อเคลื่อนที่ไปทางขวา
    def move_right(self):
        self.x += self.speed  # ความเร็วเคลื่อนที่ไปทางขวา

    # เพิ่มเมทอด move_left() เพื่อเคลื่อนที่ไปทางซ้าย
    def move_left(self):
        self.x -= self.speed  # ความเร็วเคลื่อนที่ไปทางซ้าย

    def draw(self):
        # วาดรูปภาพตัวละครบนหน้าต่าง screen ในตำแหน่ง (self.x, self.y)
        screen.blit(self.animation_frames[self.animation_frame], (self.x, self.y))

class Floor:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

floors = []
for i in range(40):  # สร้าง 10 ชิ้นของพื้นหลัง floor ต่อกัน
    floor = Floor(i * floor_width, 600, floor_image)
    floors.append(floor)

# สร้างอ็อบเจกต์ Player
player = Player(200, 495, 90, 110)
# สร้างอ็อบเจกต์ Floor
floor = Floor(0, 600, floor_image)

# คำนวณความเร็วของพื้นหลัง
background_speed = 0.01

running = True
last_frame_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ตรวจสอบการกดปุ่มลูกศรขวา
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT]:
    #     player.move_right()
 
    # elif keys[pygame.K_LEFT]:
    #     player.move_left()

    # คำนวณการเคลื่อนที่ของพื้นหลัง floor ตามตำแหน่งของตัวละคร
    for floor in floors:
        floor.move(-player.speed, 0)

    current_time = pygame.time.get_ticks()

    # ล้างหน้าต่าง
    screen.fill((0, 0, 0))

    # แสดงรูปภาพพื้นหลัง
    # screen.fill("white")
    screen.blit(background_combined, (background_x, 0))
    print(background_x)

    # แสดงตัวละคร
    player.draw()
    # แสดงพื้นหลัง floor ต่อกัน
    for floor in floors:
        floor.draw()

    # อัปเดตหน้าต่าง
    pygame.display.flip()

    # อัปเดตตำแหน่งของพื้นหลัง
    background_x -= background_speed

    # สลับภาพพื้นหลังเมื่อค่า x ต่ำกว่าค่าที่ต้องการให้เริ่มภาพใหม่
    if background_x < -4000:
        background_x = -2000

    # คำนวณเวลา
    if current_time - last_frame_time >= player.frame_delay:
        player.animation_frame = (player.animation_frame + 1) % len(player.animation_frames)
        last_frame_time = current_time

pygame.quit()