'''
Vamos a determinar el tamaño de la pantalla.
'''

import pygame

pygame.init()
info = pygame.display.Info()
width = info.current_w
height = info.current_h

screen = pygame.display.set_mode((width, height))

print(info)
print(width)
print(height)