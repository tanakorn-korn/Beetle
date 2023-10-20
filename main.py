import pygame
pygame.init()

# กำหนดขนาดหน้าต่างเกม
screen = pygame.display.set_mode((800, 600))

# กำหนดชื่อหน้าต่าง
pygame.display.set_caption("My Game")

# ลูปหลักของเกม
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()