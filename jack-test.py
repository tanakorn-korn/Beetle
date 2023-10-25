# Example file showing a circle moving on screen
# pylint: disable=no-member
import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()

# สร้างหน่วยความเร็วในการลด HP ทุกๆ 1 วินาที
hp_reduction_speed = 1000  # หน่วยเป็นมิลลิวินาที (1000 มิลลิวินาที = 1 วินาที)
last_hp_reduction_time = pygame.time.get_ticks()

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

        self.hp_bar = HPBar(50, 50, 10, 'static/image/gui/png/Windows_46.png')
        self.current_hp = 10  # HP สูงสุด
        self.damage_per_second = 1  # ความเสียหายต่อวินาที


        # กำหนด self.animation_frames ให้เริ่มจาก self.standing_frames
        self.animation_frames = self.standing_frames  

        self.animation_frame = 0
        self.frame_rate = 10
        self.frame_delay = 1000 / self.frame_rate
        self.is_sitting = False
        self.is_runing = False
        self.jumping = False
        self.on_floor = True 

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
        if not self.jumping and self.on_floor:  # ตรวจสอบว่ายังไม่กระโดดและอยู่บนพื้น
            self.jumping = True
            self.animation_frames = self.jumping_frames
            self.jump_height = 0
            self.jump_speed = -2.5
        elif not self.jumping and not self.on_floor:  # ไม่สามารถกระโดดถ้าไม่อยู่บนพื้น
            pass
        else:
            self.animation_frames = self.standing_frames

    def draw(self):
        if 0 <= self.animation_frame < len(self.animation_frames):
            screen.blit(self.animation_frames[self.animation_frame], self.rect.topleft)
        
        self.hp_bar.draw(screen)
    
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


class HPBar:
    def __init__(self, x, y, max_hp, hp_image_path):
        self.x = x
        self.y = y
        self.max_hp = max_hp  # HP สูงสุด
        self.current_hp = max_hp  # คำนวณ HP ปัจจุบัน
        self.hp_images = [pygame.image.load(hp_image_path) for _ in range(max_hp)]

    def decrease_hp(self, amount):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0

    def increase_hp(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def draw(self, screen):
        for i in range(self.current_hp):
            screen.blit(self.hp_images[i], (self.x + i * self.hp_images[i].get_width(), self.y))


# สร้างรายการ floor โดยสุ่มความสูงของพื้น
floors = [Floor(i * floor_width, random.randint(500, 620)) for i in range(40)]

player = Player(200, 460, 90, 110)


running = True
jumping = False
last_frame_time = pygame.time.get_ticks()

while running:
    current_time = pygame.time.get_ticks()

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
    
    # ตรวจสอบเวลาลด HP
    if current_time - last_hp_reduction_time >= hp_reduction_speed:
        player.hp_bar.decrease_hp(1)  # ลด HP ลงทีละ 1 หน่วย
        last_hp_reduction_time = current_time

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
    print(last_hp_reduction_time)
    player.hp_bar.draw(screen)

    pygame.display.flip()
    background_x -= player.background_speed

    if background_x < -4000:
        background_x = -2000

    if current_time - last_frame_time >= player.frame_delay:
        player.animation_frame = (player.animation_frame + 1) % len(player.animation_frames)
        last_frame_time = current_time

pygame.quit()
