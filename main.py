import pygame
import math
import sys

# Khởi tạo Pygame
pygame.init()

# Khai báo hằng số
WIDTH, HEIGHT = 816, 489
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
AZURE = (240, 255, 255)

# Thiết lập màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mô Phỏng Trục Khuỷu")

# Xác định tốc độ ban đầu
speed = 1

# Xác định các thông số của trục khuỷu và piston
crank_radius = 80
rod_length = 150
angle = 270

org = (200, 200)  # Gốc của trục khuỷu (tâm của đường tròn)
cylinder_width = 220
cylinder_height = 80
cylinder_x = 450
cylinder_y = org[1] - cylinder_height // 2

piston_width = 50
piston_height = 80
min_piston_x = cylinder_x
max_piston_x = cylinder_x + cylinder_width - piston_width

# Hàm trợ giúp để tính toán điểm trên đường tròn
def circle_point(radius, angle_in_degrees, origin):
    angle_in_radians = math.radians(angle_in_degrees)
    x = origin[0] + radius * math.cos(angle_in_radians)
    y = origin[1] + radius * math.sin(angle_in_radians)
    return (x, y)

# Vòng lặp chính
running = True
while running:
    screen.fill(BLACK)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed += 1.0
            elif event.key == pygame.K_DOWN:
                speed = max(0.5, speed - 1.0)
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Tính toán vị trí
    loc = circle_point(crank_radius, angle, org)
    opposite_loc = circle_point(crank_radius, angle + 180, org)
    piston_x = cylinder_x + (loc[0] - org[0]) + crank_radius
    piston_x = max(min_piston_x, min(piston_x, max_piston_x))
    piston_center = (piston_x + piston_width // 2, cylinder_y + (cylinder_height - piston_height) // 2 + piston_height // 2)

    # Vẽ đường tròn của trục khuỷu
    pygame.draw.circle(screen, AZURE, (int(org[0]), int(org[1])), crank_radius, 3)
    pygame.draw.circle(screen, YELLOW, (int(org[0]), int(org[1])), 5)  # Điểm trung tâm

    # Vẽ thanh nối
    pygame.draw.line(screen, AZURE, loc, piston_center, 3)
    pygame.draw.circle(screen, RED, (int(loc[0]), int(loc[1])), 5)  # Điểm di chuyển trên đường tròn
    pygame.draw.circle(screen, RED, (int(opposite_loc[0]), int(opposite_loc[1])), 5)  # Điểm đối diện

    # Vẽ piston
    pygame.draw.rect(screen, WHITE, (piston_x, cylinder_y + (cylinder_height - piston_height) // 2, piston_width, piston_height))

    # Vẽ xi-lanh
    top_left = (cylinder_x, cylinder_y)
    top_right = (cylinder_x + cylinder_width, cylinder_y)
    bottom_left = (cylinder_x, cylinder_y + cylinder_height)
    bottom_right = (cylinder_x + cylinder_width, cylinder_y + cylinder_height)
    pygame.draw.line(screen, WHITE, top_left, top_right, 3)
    pygame.draw.line(screen, WHITE, bottom_left, bottom_right, 3)
    pygame.draw.line(screen, WHITE, top_right, bottom_right, 3)

    #nối hai điểm màu đỏ đi qia tâm trục khuỷu
    pygame.draw.line(screen, RED, loc, opposite_loc, 3)


    # Các đường thẳng dọc ở bên trái của xi-lanh
    pygame.draw.line(screen, WHITE, top_left, (cylinder_x, cylinder_y - 20), 3)
    pygame.draw.line(screen, WHITE, bottom_left, (cylinder_x, cylinder_y + cylinder_height + 20), 3)

    font = pygame.font.Font(None, 24)
    text = font.render("Speed: " + "x"+str(int(speed)), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    # Cập nhật góc
    angle += speed * 0.5
    if angle >= 360:
        angle = 0

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều chỉnh tốc độ khung hình
    pygame.time.delay(10)

# Kết thúc chương trình
pygame.quit()
sys.exit()
