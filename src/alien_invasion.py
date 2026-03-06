import pygame
import sys

class AlienInvasion:
    '''Clase general para gestionar los recursos y el comportamiento del juego'''

    def __init__(self):
        '''Inicializa el juego y crea recursos del juego'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)
        '''Configura el color de fondo.'''

    def run_game(self):
        '''Inicia el bucle principal para el juego'''
        while True:
            '''Busca eventos de teclado y ratón'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            '''Redibuja la patalla en cada paso por el bucle'''
            pygame.display.flip()
            '''Hace visible la última pantalla dibujada.'''
            self.clock.tick(60)

if __name__ == '__main__':
    '''Hace una instancia del juego y lo ejecuta'''
    ai = AlienInvasion()
    ai.run_game()
