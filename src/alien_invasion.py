import pygame
import sys

from settings import Settings
from ship import Ship           #Importamos Ship()

class AlienInvasion:
    '''Clase general para gestionar los recursos y el comportamiento del juego'''

    def __init__(self):
        '''Inicializa el juego y crea recursos del juego'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  #La llamada a Ship() requiere un argumento, una instancia de AlienInvasion
                                #El parámetro da a Ship acceso a los recursos del juego.

    def run_game(self):
        '''Inicia el bucle principal para el juego'''
        while True:
            '''Busca eventos de teclado y ratón'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            '''Redibuja la patalla en cada paso por el bucle'''

            self.ship.blitme()  #Dibujamos la nave en la pantalla.

            pygame.display.flip()
            '''Hace visible la última pantalla dibujada.'''
            self.clock.tick(60)

if __name__ == '__main__':
    '''Hace una instancia del juego y lo ejecuta'''
    ai = AlienInvasion()
    ai.run_game()
