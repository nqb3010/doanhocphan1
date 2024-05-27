import pygame
import math
import sys
# Khởi tạo Pygame
pygame.init()
angle = 360  # Góc ban đầu
radius = 90  # Bán kính của hình tròn
center_x = 120  # Tọa độ x của tâm hình tròn
center_y = 300  # Tọa độ y của tâm hình tròn
# Tạo màn hình
speed = 1
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Piston")
# Tạo danh sách chứa các đoạn thẳng
lines = [((400, 240), (400, 260)),
          ((400, 260), (700, 260)), 
         ((700, 260), (700, 345)),  
         ((700, 345), (400, 345)),
         ((400, 365), (400, 345))]   

# Vị trí ban đầu của hình ảnh
x = 400
y = 300
# Biến kiểm soát hướng tăng giảm của x
increasing = True
# Biến kiểm soát vòng lặp chính
running = True
# Vòng lặp chính
while True:

    #fps = 60
    clock = pygame.time.Clock()
    clock.tick(60)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
            elif event.key == pygame.K_UP:
                speed += 1  # Tăng tốc độ quay khi nhấn phím mũi tên lên
            elif event.key == pygame.K_DOWN:
                     if speed >0:
                            speed -= 1  # Giảm tốc độ quay khi nhấn phím mũi tên xuống
                # Xóa màn hình
    screen.fill((0, 0, 0))
    #
    # Vẽ các đoạn thẳng
    for line in lines:
        pygame.draw.line(screen, (255, 255, 255), line[0], line[1], 6)
    #vẽ hình vuông

    point_x = center_x + int(radius * math.cos(math.radians(angle)))
    point_y = center_y + int(radius * math.sin(math.radians(angle)))
    # điểm đối xứng của point_x và point_y qua tâm hình tròn
    px = 2 * center_x - point_x
    py = 2 * center_y - point_y
    # Vẽ hình ảnh lên màn hình
    if x >= 620:
        increasing = False  # Khi x đạt 650, thay đổi hướng giảm dần
    if increasing:
        pygame.time.delay(10)
        x += 1.5 * speed  # Tăng giá trị của x nếu đang trong quá trình tăng
    else:
        pygame.time.delay(10)
        x -= 1 * speed  # Giảm giá trị của x nếu đang trong quá trình giảm

    if x <= 400:  # Khi x giảm về 299, thoát khỏi vòng lặp
        increasing = True
    pygame.time.delay(10)
    angle += 1 * speed
    if angle >= 360:
        # Khi góc quay đạt 180 độ dừng lại
        angle = 0

    # Vẽ dây nối từ trục quay tới hình ảnh piston
    pygame.draw.line(screen, (255, 255, 255), (point_x, point_y), (x, y), 5)
    pygame.draw.line(screen, (255, 255, 255), (120, 300), (point_x, point_y), 1)
    pygame.draw.line(screen, (255, 255, 255), (120, 300), (px, py), 1)
    #vẽ điểm ở tâm hình tròn
    pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), 5)
    # Vẽ hình tròn và điểm trên hình tròn
    pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), radius, 1)
    pygame.draw.circle(screen, (255, 0, 0), (int(point_x), int(point_y)), 5)
    # Vẽ hình ảnh piston
    pygame.draw.rect(screen, (255, 255, 255), (x, y-36, 80, 80))

    pygame.display.update()