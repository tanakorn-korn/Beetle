# # Example file showing a circle moving on screen
# # pylint: disable=no-member
# import pygame
# import random
# # import pdb

# pygame.init()
# screen = pygame.display.set_mode((1200, 720))
# clock = pygame.time.Clock()

# background_combined = pygame.image.load('static/image/graveyardtilesetnew/png/BG_combined-1.png').convert()
# background_x = -2000

# floor_image = pygame.image.load('static/image/graveyardtilesetnew/png/Tiles/Tile (2).png').convert()
# floor_width = floor_image.get_width()


# class Player:
#     def __init__(self, x, y, width, height):
#         self.background_speed = 0.01
#         self.speed = 0.2
#         self.x = x
#         self.y = y
#         self.standing_frames = [
#             pygame.image.load('static/image/jackfree/png/Walk (1).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (2).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (3).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (4).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (5).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (6).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (7).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (8).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (9).png'),
#             pygame.image.load('static/image/jackfree/png/Walk (10).png')
#         ]
#         self.sitting_frames = [
#             pygame.image.load('static/image/jackfree/png/Slide (1).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (2).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (3).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (4).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (5).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (6).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (7).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (8).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (9).png'),
#             pygame.image.load('static/image/jackfree/png/Slide (10).png')
#         ]
#         self.runing_frames = [
#             pygame.image.load('static/image/jackfree/png/Run (1).png'),
#             pygame.image.load('static/image/jackfree/png/Run (2).png'),
#             pygame.image.load('static/image/jackfree/png/Run (3).png'),
#             pygame.image.load('static/image/jackfree/png/Run (4).png'),
#             pygame.image.load('static/image/jackfree/png/Run (5).png'),
#             pygame.image.load('static/image/jackfree/png/Run (6).png'),
#             pygame.image.load('static/image/jackfree/png/Run (7).png'),
#             pygame.image.load('static/image/jackfree/png/Run (8).png'),
#         ]
#         self.standing_frames = [pygame.transform.scale(frame, (width, height)) for frame in self.standing_frames]
#         self.sitting_frames = [pygame.transform.scale(frame, (width, height - 20)) for frame in self.sitting_frames]  # ปรับความสูง
#         self.runing_frames = [pygame.transform.scale(frame, (width, height)) for frame in self.runing_frames]
#         self.rect = self.animation_frames[self.animation_frame].get_rect(topleft=(self.x, self.y))


#         self.animation_frames = self.standing_frames
#         self.animation_frame = 0
#         self.frame_rate = 10
#         self.frame_delay = 1000 / self.frame_rate
#         self.is_sitting = False  # เพิ่มตัวแปรสถานะนั่ง/ยืน
#         self.is_runing = False  # เพิ่มตัวแปรสถานะวิ่ง

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#         self.rect.move_ip(dx, dy)

#     def toggle_sitting(self):
#         if self.is_sitting:
#             self.is_sitting = False
#             self.animation_frames = self.standing_frames
#             self.y += -20
#         else:
#             self.is_sitting = True
#             self.animation_frames = self.sitting_frames
#             self.y -= -20
    
#     def toggle_runing(self):
#         if self.is_runing:
#             self.is_runing = False
#             self.animation_frames = self.standing_frames
#             self.speed = 0.2
#             self.background_speed = 0.01
#         else:
#             self.is_runing = True
#             self.animation_frames = self.runing_frames
#             self.speed = 0.5
#             self.background_speed = 0.03

#     def draw(self):
#         if 0 <= player.animation_frame < len(player.animation_frames):
#             screen.blit(player.animation_frames[player.animation_frame], (player.x, player.y))
        
#         collision = False
#         for floor in floors:
#             if self.rect.colliderect(floor.get_rect()):
#                 collision = True
#                 break

#         if not collision:
#             # ถ้าไม่มีการชนกับ floor ใด ๆ ให้เคลื่อนตัวละคร
#             self.move(self.speed, 0)

#         if 0 <= self.animation_frame < len(self.animation_frames):
#             screen.blit(self.animation_frames[self.animation_frame], self.rect.topleft)

#     def check_collision(self, floor):
#         if 0 <= self.animation_frame < len(self.animation_frames):
#             player_rect = self.animation_frames[self.animation_frame].get_rect(topleft=(self.x, self.y))
#             floor_rect = floor.image.get_rect(topleft=(floor.x, floor.y))
#             floor_rect = floor.get_rect()
#             return player_rect.colliderect(floor_rect)
        
        
#         return False
    
#     def update(self):
#         # เพิ่มบรรทัดนี้เพื่ออัปเดตตำแหน่งของผู้เล่น
#         self.rect.topleft = (self.x, self.y)



# class Floor:
#     def __init__(self, x, y, image):
#         self.x = x
#         self.y = y
#         self.image = image
#         self.rect = image.get_rect(topleft=(x, y))

#     # def move(self, dx, dy):
#     #     self.x += dx
#     #     self.y += dy

#     def draw(self):
#         screen.blit(self.image, (self.x, self.y))

#     def get_rect(self):
#         return self.rect

# # เพิ่มรายการ floor ในรายการ floors
# floors = []
# for i in range(40):
#     floor_x = 0 + i * floor_width  # ตั้งค่า x ที่ x = 2000 และเพิ่มขึ้นเรื่อย ๆ
#     floor_y = random.randint(500, 620)  # สุ่มความสูงของ floor ระหว่าง 500 ถึง 620
#     floor = Floor(floor_x, floor_y, floor_image)
#     floors.append(floor)

# # floors = []
# # for i in range(10):
# #     floor = Floor(i * floor_width, 600, floor_image)
# #     floors.append(floor)

# player = Player(200, 460, 90, 110)
# floor = Floor(0, 600, floor_image)


# running = True
# last_frame_time = pygame.time.get_ticks()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_DOWN]:
#         if not player.is_sitting:
#             player.toggle_sitting()
#         down_pressed = True
#     else:
#         if player.is_sitting:
#             player.toggle_sitting()
#         down_pressed = False

#     if not down_pressed:
#         if keys[pygame.K_RIGHT]:
#             if not player.is_runing:
#                 player.toggle_runing()
#         elif player.is_runing:
#             player.toggle_runing()
 

#     player_on_floor = False
#     for floor in floors:
#         if player.check_collision(floor):
#             player_on_floor = True
#             player.y = floor.y - player.animation_frames[0].get_height()
#             break
    

#     if not player_on_floor:
#         player.y += player.speed  # อยู่ในอากาศเนื่องจากไม่มีพื้น

#     for floor in floors:
#         floor.move(-player.speed, 0)
#         floor.rect.topleft = (floor.x, floor.y)

#     player.update()  # เรียกฟังก์ชันอัปเดตผู้เล่น

#     if player.check_collision(floor):
#         player.speed = 0.0
#         player.y = floor.y - player.rect.height
#     else:
#         player.speed = 0.2
#         player.background_speed = 0.01

#     current_time = pygame.time.get_ticks()

#     screen.fill((0, 0, 0))
#     screen.blit(background_combined, (background_x, 0))

#     # เรียกเมทอด draw ของ player เพื่อวาดตัวละครและตรวจสอบการชนกับ floor
#     player.draw()
   
#     for floor in floors:
#         floor.draw()
    
#     player.draw()

#     pygame.display.flip()
#     background_x -= player.background_speed

#     if background_x < -4000:
#         background_x = -2000

#     if current_time - last_frame_time >= player.frame_delay:
#         player.animation_frame = (player.animation_frame + 1) % len(player.animation_frames)
#         last_frame_time = current_time
        

# pygame.quit()



# Example file showing a circle moving on screen
# pylint: disable=no-member
# Example file showing a circle moving on screen
# pylint: disable=no-member
import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()

background_combined = pygame.image.load('static/image/graveyardtilesetnew/png/BG_combined-1.png').convert()
background_x = -2000

floor_image = pygame.image.load('static/image/graveyardtilesetnew/png/Tiles/Tile (2).png').convert()
floor_width = floor_image.get_width()

class Player:
    def __init__(self, x, y, width, height):
        self.background_speed = 0.01
        self.speed = 0.5
        self.x = x
        self.y = y
        self.standing_frames = [
            pygame.image.load('static/image/jackfree/png/Walk (1).png'),
            pygame.image.load('static/image/jackfree/png/Walk (2).png'),
            pygame.image.load('static/image/jackfree/png/Walk (3).png'),
            pygame.image.load('static/image/jackfree/png/Walk (4).png'),
            pygame.image.load('static/image/jackfree/png/Walk (5).png'),
            pygame.image.load('static/image/jackfree/png/Walk (6).png'),
            pygame.image.load('static/image/jackfree/png/Walk (7).png'),
            pygame.image.load('static/image/jackfree/png/Walk (8).png'),
            pygame.image.load('static/image/jackfree/png/Walk (9).png'),
            pygame.image.load('static/image/jackfree/png/Walk (10).png')
        ]
        self.sitting_frames = [
            pygame.image.load('static/image/jackfree/png/Slide (1).png'),
            pygame.image.load('static/image/jackfree/png/Slide (2).png'),
            pygame.image.load('static/image/jackfree/png/Slide (3).png'),
            pygame.image.load('static/image/jackfree/png/Slide (4).png'),
            pygame.image.load('static/image/jackfree/png/Slide (5).png'),
            pygame.image.load('static/image/jackfree/png/Slide (6).png'),
            pygame.image.load('static/image/jackfree/png/Slide (7).png'),
            pygame.image.load('static/image/jackfree/png/Slide (8).png'),
            pygame.image.load('static/image/jackfree/png/Slide (9).png'),
            pygame.image.load('static/image/jackfree/png/Slide (10).png')
        ]
        self.runing_frames = [
            pygame.image.load('static/image/jackfree/png/Run (1).png'),
            pygame.image.load('static/image/jackfree/png/Run (2).png'),
            pygame.image.load('static/image/jackfree/png/Run (3).png'),
            pygame.image.load('static/image/jackfree/png/Run (4).png'),
            pygame.image.load('static/image/jackfree/png/Run (5).png'),
            pygame.image.load('static/image/jackfree/png/Run (6).png'),
            pygame.image.load('static/image/jackfree/png/Run (7).png'),
            pygame.image.load('static/image/jackfree/png/Run (8).png'),
        ]
        self.jumping_frames = [
            pygame.image.load('static/image/jackfree/png/Jump (1).png'),
            pygame.image.load('static/image/jackfree/png/Jump (2).png'),
            pygame.image.load('static/image/jackfree/png/Jump (3).png'),
            pygame.image.load('static/image/jackfree/png/Jump (4).png'),
            pygame.image.load('static/image/jackfree/png/Jump (5).png'),
            pygame.image.load('static/image/jackfree/png/Jump (6).png'),
            pygame.image.load('static/image/jackfree/png/Jump (7).png'),
            pygame.image.load('static/image/jackfree/png/Jump (8).png'),
            pygame.image.load('static/image/jackfree/png/Jump (9).png'),
            pygame.image.load('static/image/jackfree/png/Jump (10).png'),
        ]
        self.standing_frames = [pygame.transform.scale(frame, (width, height)) for frame in self.standing_frames]
        self.sitting_frames = [pygame.transform.scale(frame, (width, height - 20)) for frame in self.sitting_frames]
        self.runing_frames = [pygame.transform.scale(frame, (width, height)) for frame in self.runing_frames]
        self.jumping_frames = [pygame.transform.scale(frame, (width, height)) for frame in self.jumping_frames]

        # กำหนด self.animation_frames ให้เริ่มจาก self.standing_frames
        self.animation_frames = self.standing_frames  

        self.animation_frame = 0
        self.frame_rate = 10
        self.frame_delay = 1000 / self.frame_rate
        self.is_sitting = False
        self.is_runing = False
        self.jumping = False
        self.rect = self.animation_frames[self.animation_frame].get_rect(topleft=(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.move_ip(dx, dy)

    def toggle_sitting(self):
        if not self.is_sitting:
            self.is_sitting = True
            self.animation_frames = self.sitting_frames
            self.y += 0  # ปรับค่าตามความสูงที่คุณต้องการ
        else:
            self.is_sitting = False
            self.animation_frames = self.standing_frames
            self.y -= 0  # ปรับค่าตามความสูงที่คุณต้องการ
    
    def toggle_runing(self):
        if self.is_runing:
            self.is_runing = False
            self.animation_frames = self.standing_frames
            self.speed = 0.5
            self.background_speed = 0.01
        else:
            self.is_runing = True
            self.animation_frames = self.runing_frames
            self.speed = 0.8
            self.background_speed = 0.03
    
    def toggle_jumping(self):
        if not self.jumping:  # ตรวจสอบว่ายังไม่ได้กระโดดก่อน
            self.jumping = True
            self.animation_frames = self.jumping_frames
            self.jump_height = 0  # เพิ่มตัวแปรเก็บความสูงของกระโดด
            self.jump_speed = -1.5  # ปรับค่าตามสไปด์ของเกมของคุณ
        else:
            self.jump_height = 0  # รีเซ็ตความสูงของกระโดด
            self.jump_speed = -1.5  # รีเซ็ตความเร็วของกระโดด
            self.animation_frames = self.jumping_frames  # เปลี่ยนเป็นอนิเมชันกระโดด

    def draw(self):
        if 0 <= self.animation_frame < len(self.animation_frames):
            screen.blit(self.animation_frames[self.animation_frame], self.rect.topleft)
    
    def check_collision(self, floor):
        if 0 <= self.animation_frame < len(self.animation_frames):
            player_rect = self.animation_frames[self.animation_frame].get_rect(topleft=(self.x, self.y))
            floor_rect = floor.image.get_rect(topleft=(floor.x, floor.y))
            floor_rect = floor.get_rect()
            return player_rect.colliderect(floor_rect)
        return False

    def update(self):
        # เพิ่มบรรทัดนี้เพื่ออัปเดตตำแหน่งของ player.rect
        self.rect.topleft = (self.x, self.y)

        if self.jumping:
            self.jump_height += self.jump_speed
            self.y += self.jump_speed

            if self.jump_height < -150:  # ปรับค่าตามความสูงของกระโดด
                self.jump_speed = 2
                self.animation_frames = self.standing_frames
            if self.jump_height >= 0:
                self.jumping = False

                

class Floor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = floor_image
        self.rect = floor_image.get_rect(topleft=(x, y))

    def draw(self):
        screen.blit(self.image, self.rect.topleft)

    def get_rect(self):
        return self.rect

# สร้างรายการ floor โดยสุ่มความสูงของพื้น
floors = [Floor(i * floor_width, random.randint(500, 620)) for i in range(40)]

player = Player(200, 460, 90, 110)

running = True
jumping = False
last_frame_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        if not player.is_sitting:
            player.toggle_sitting()
        down_pressed = True
    else:
        if player.is_sitting:
            player.toggle_sitting()
        down_pressed = False

    # ตรวจสอบว่าปุ่ม "spec" ถูกกดหรือไม่ และกระโดดเมื่อกดปุ่ม
    if keys[pygame.K_SPACE] and not jumping:
        player.toggle_jumping()
        print("Jumping!")
        jumping = True
    if not keys[pygame.K_SPACE]:
        jumping = False
    pygame.display.update()

    if not down_pressed:
        if keys[pygame.K_RIGHT]:
            if not player.is_runing:
                player.toggle_runing()
        elif player.is_runing:
            player.toggle_runing()

    player_on_floor = False
    for floor in floors:
        if player.rect.colliderect(floor.rect):
            player_on_floor = True
            if player.y < floor.y:
                player.y = floor.y - player.rect.height
            break

    if not player_on_floor:
        player.y += 0.7

    player.update()  # เพิ่มบรรทัดนี้เพื่ออัปเดตตำแหน่งของผู้เล่น
    for floor in floors:
        floor.x -= player.speed
        floor.rect.topleft = (floor.x, floor.y)

    current_time = pygame.time.get_ticks()

    screen.fill((0, 0, 0))
    screen.blit(background_combined, (background_x, 0))
   
    for floor in floors:
        floor.draw()
    
    player.draw()

    pygame.display.flip()
    background_x -= player.background_speed

    if background_x < -4000:
        background_x = -2000

    if current_time - last_frame_time >= player.frame_delay:
        player.animation_frame = (player.animation_frame + 1) % len(player.animation_frames)
        last_frame_time = current_time

pygame.quit()
