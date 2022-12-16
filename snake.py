import pygame
from pygame.locals import *

SIZE = 40

class Snake :
    def __init__(self, surface, lenght): 
        # On récupère la longueur du serpent
        self.length = lenght
        # On récupère la surface de l'écran
        self.parent_screen = surface
        # On charge l'image du block
        self.block = pygame.image.load("resources/snake.jpg").convert()
        # On récupère les coordonnées du block
        self.x = [SIZE]*lenght
        self.y = [SIZE]*lenght
        # On récupère la direction du block
        self.direction = 'right'

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    # fonctions pour faire bouger le block
    def move_left(self):
        if self.direction == 'right':
            return
        else:
            self.direction = 'left'

    def move_right(self):
        if self.direction == 'left':
            return
        else:
            self.direction = 'right'

    def move_up(self):
        if self.direction == 'down':
            return
        else:
            self.direction = 'up'

    def move_down(self):   
        if self.direction == 'up':
            return
        else:
            self.direction = 'down'

    def walk(self):
        # on fait bouger les blocks du serpent qui ne sont pas la tête
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        #  on fait bouger la tête du serpent
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()

    def draw(self):
        for i in range(self.length):
            # On dessine le block sur la nouvelle surface de l'écran
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        # On met à jour l'écran
        pygame.display.flip()
