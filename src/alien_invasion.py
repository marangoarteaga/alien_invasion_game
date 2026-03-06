import pygame
import sys

class AlienInvasion:
    '''Clase general para gestionar los recursos y el comportamiento del juego'''

    def __init__(self):
        '''Inicializa el juego y crea recursos'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Alien Invasion")

    def run_game():
        '''Inicia el bucle principal para el juego'''
        while True:
            '''Busca eventos de teclado y ratón'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            '''Hace visible la última pantalla dibujada.'''

if __name__ == '__main__':
    '''Hace una instancia del juego y lo ejecuta'''
ai = AlienInvasion()
ai.run_game()
