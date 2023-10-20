# Example file showing a circle moving on screen
# pylint: disable=no-member
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

# # โหลดรูปภาพ animation
# animation_frames = [
#     pygame.image.load('static/image/jackfree/png/Walk (1).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (2).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (3).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (4).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (5).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (6).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (7).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (8).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (9).png'),
#     pygame.image.load('static/image/jackfree/png/Walk (10).png'),
    
#     # เพิ่มรูปภาพเฟรมอื่น ๆ ตรงนี้
# ]

# # ตำแหน่งเริ่มต้นของ animation
# animation_frame = 0
# frame_rate = 10  # อัตราเฟรมต่อวินาที
# frame_delay = 1000 / frame_rate  # คำนวณเวลาที่ต้องรอระหว่างเฟรม

# running = True
# last_frame_time = pygame.time.get_ticks()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # คำนวณเวลา
#     current_time = pygame.time.get_ticks()
#     if current_time - last_frame_time >= frame_delay:
#         # แสดงเฟรมถัดไปใน animation
#         animation_frame = (animation_frame + 1) % len(animation_frames)
#         last_frame_time = current_time

#     # ล้างหน้าต่าง
#     screen.fill((0, 0, 0))

#     # แสดง animation frame ปัจจุบัน
#     screen.blit(animation_frames[animation_frame], (0, 0))

#     # อัปเดตหน้าต่าง
#     pygame.display.flip()

# pygame.quit()