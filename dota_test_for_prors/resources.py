import pygame
from time import time
class Ti_image():

    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load("dota_ti.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50

    def blitme(self):
        self.screen.blit(self.image,self.rect)

class Button():

    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0,125,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.msg_image = self.font.render("start",True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


class Board():

    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,32)


    def flash(self,start_time,gamestat,click_num):
        self.click_num = click_num
        if gamestat == True and 60-(time() - start_time) > 0:
            self.second_left = 60-(time() - start_time)
        elif 60-(time() - start_time) < 0:
            self.second_left = 0
        else:
            self.second_left = 60
        second_str = "Time remaining " + str(int(self.second_left)) + "s"
        click_str = "Click numbers " + str(self.click_num)
        show_string = second_str + "         " + click_str
        self.show_image = self.font.render(show_string, True, self.text_color, (230, 230, 230))

        self.show_rect = self.show_image.get_rect()
        self.show_rect.centerx = self.screen_rect.centerx
        self.show_rect.top = 20

        self.screen.blit(self.show_image,self.show_rect)


