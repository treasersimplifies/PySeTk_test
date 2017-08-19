import sys
import pygame
from resources import *
from time import *


def main():
    bg_color = (230, 230, 230)
    with open("record.txt") as record:
        record_clicks = int(record.read())
    pygame.init()
    screen = pygame.display.set_mode((800,550))
    pygame.display.set_caption("1分钟鼠标点击测试")
    gamestat = False
    click_num = 0
    picture = Ti_image(screen)
    button = Button(screen)
    board = Board(screen)
    start_time = time()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if int(click_num) > record_clicks:
                    with open("record.txt","w") as record:
                        record.write(str(click_num))
                print(str(click_num))
                print(str(time()-start_time))
                sys.exit(0)
            elif event.type ==pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button.rect.collidepoint(mouse_x,mouse_y):
                    gamestat = True
                    start_time = time()
                if gamestat == True and picture.rect.collidepoint(mouse_x,mouse_y) and time()-start_time < 60 and not button.rect.collidepoint(mouse_x,mouse_y):
                    click_num += 1
        screen.fill(bg_color)
        picture.blitme()
        if gamestat == False:
            button.draw_button()
        board.flash(start_time,gamestat,click_num)
        pygame.display.flip()


main()

