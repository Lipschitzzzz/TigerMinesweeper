import pygame
import sys
import numpy as np
import random
def is_there_a_mine(mat, mat_1, index1,index2):
    if mat[ index2[0] ][ index2[1] ] == 99:
        mat_1[ index1[0] ][ index1[1] ] += 1
    return mat_1
def mines_around(mat, mat_1):
    is_there_a_mine(mat, mat_1, [0, 0], [1, 0])
    is_there_a_mine(mat, mat_1, [0, 0], [0, 1])
    is_there_a_mine(mat, mat_1, [9, 0], [8, 0])
    is_there_a_mine(mat, mat_1, [9, 0], [9, 1])
    is_there_a_mine(mat, mat_1, [0, 9], [0, 8])
    is_there_a_mine(mat, mat_1, [0, 9], [1, 9])
    is_there_a_mine(mat, mat_1, [9, 9], [9, 8])
    is_there_a_mine(mat, mat_1, [9, 9], [8, 9])
    for i in range(1,9):
        if (mat[0, i] or mat[9, i]) == 99:
            continue
        is_there_a_mine(mat, mat_1, [0, i], [0, i - 1])
        is_there_a_mine(mat, mat_1, [0, i], [0, i + 1])
        is_there_a_mine(mat, mat_1, [0, i], [1, i])
        is_there_a_mine(mat, mat_1, [9, i], [9, i - 1])
        is_there_a_mine(mat, mat_1, [9, i], [9, i + 1])
        is_there_a_mine(mat, mat_1, [9, i], [8, i])
    for i in range(1,9):
        if (mat[i, 0] or mat[i, 9]) == 99:
            continue
        is_there_a_mine(mat, mat_1, [i, 0], [i - 1, 0])
        is_there_a_mine(mat, mat_1, [i, 0], [i + 1, 0])
        is_there_a_mine(mat, mat_1, [i, 0], [i, 1])
        is_there_a_mine(mat, mat_1, [i, 9], [i - 1, 9])
        is_there_a_mine(mat, mat_1, [i, 9], [i + 1, 9])
        is_there_a_mine(mat, mat_1, [i, 9], [i, 8])
    for i in range(1,9):
        for j in range(1,9):
            if (mat[i, j]) == 99:
                continue
            is_there_a_mine(mat, mat_1, [i, j], [i - 1, j])
            is_there_a_mine(mat, mat_1, [i, j], [i + 1, j])
            is_there_a_mine(mat, mat_1, [i, j], [i, j - 1])
            is_there_a_mine(mat, mat_1, [i, j], [i, j + 1])
            is_there_a_mine(mat, mat_1, [i, j], [i - 1, j - 1])
            is_there_a_mine(mat, mat_1, [i, j], [i + 1, j + 1])
            is_there_a_mine(mat, mat_1, [i, j], [i + 1, j - 1])
            is_there_a_mine(mat, mat_1, [i, j], [i - 1, j + 1])
    return mat_1
def draw_background(screen):
    # 填充背景色
    screen.fill((255, 255, 255))
    # 画外框
    outer_frame_color = (0, 0, 0)
    pygame.draw.rect(screen, outer_frame_color, [0, 100, 800, 800], 5)
    # 列 80，100 到 800，100 共10条
    inner_frame_color = (0, 0, 0)
    for i in range(0, 11):
        pygame.draw.line(screen, inner_frame_color, (80 + 80 * i, 100), (80 + 80 * i, 900))
    # 行 0，100 到 800，100 共10条
    for i in range(0, 11):
        pygame.draw.line(screen, inner_frame_color, (0, 100 + 80 * i), (800, 100 + 80 * i))
    # 80 * 80
mat = np.zeros([10,10])
mat_1 = np.zeros([10,10])
pygame.font.init()
pygame.init()
mines = []
for i in range(0,10):
    index = random.randint(0,9)
    mat[i][index] = 99
    mat_1[i][index] = 99
    mines.append( [i, index] )
mat_1 = mines_around(mat,mat_1)
png_0 = pygame.image.load('0.png')
png_0 = pygame.transform.scale(png_0, (75, 75))
png_1 = pygame.image.load('1.png')
png_1 = pygame.transform.scale(png_1, (75, 75))
png_2 = pygame.image.load('2.png')
png_2 = pygame.transform.scale(png_2, (75, 75))
png_3 = pygame.image.load('3.png')
png_3 = pygame.transform.scale(png_3, (75, 75))
image = pygame.image.load('mine.png')
image = pygame.transform.scale(image, (75, 75))
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("扫雷")
draw_background(screen)
for i in range(0, 10):
    for j in range(0, 10):
        if mat[i][j] == 99:
            screen.blit(image, (80 * j + 5, 100 + 80 * i + 5))
print(mat_1)
my_font = pygame.font.SysFont("Monaco", 40)
text_surface = my_font.render("YOU ARE FAILED!", True, (0,0,0), (255, 255, 255))
while True:
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type ==pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if (x < 800 and y < 100):
                pygame.quit()
                exit()
            x, y = int(x / 80), int((y - 100) / 80)
            number = mat_1[y][x]
            if number == 0:
                screen.blit(png_0, (80 * x + 5, 100 + 80 * y + 5))
            elif number == 1:
                screen.blit(png_1, (80 * x + 5, 100 + 80 * y + 5))
            elif number == 2:
                screen.blit(png_2, (80 * x + 5, 100 + 80 * y + 5))
            elif number == 3:
                screen.blit(png_3, (80 * x + 5, 100 + 80 * y + 5))
            elif number == 99:
                screen.fill((0,0,0))
                screen.blit(text_surface,(400,450))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()