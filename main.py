import pygame
from pygame.locals import *
import time
import random
from snake import Snake
from apple import Apple

SIZE = 40

class Game:
    def __init__(self):
        # on initialise pygame
        pygame.init()
        # on charge le titre de la fenêtre
        pygame.display.set_caption("Snake Game")
        # on initialise le mixer de pygame
        pygame.mixer.init()
        self.play_background_music()
        
        # Taille de l'écran
        self.surface = pygame.display.set_mode((1000, 800))
        # Couleur du fond d'écran
        self.surface.fill((110, 110, 10)) 
        # On charge puis dessine le serpent   
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        # On charge puis dessine la pomme
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        # on vérifie si le serpent est sur la pomme
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        # On affiche le score
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (800, 10))

    def play_background_music(self):
        # On joue la musique de fond
        pygame.mixer.music.load("resources/bg_music.mp3")
        pygame.mixer.music.play()

    def play_sound(self, sound):
        # On joue un son
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        # On dessine le fond d'écran
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        # On fait bouger le serpent automatiquement
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        
        # on vérifie si le serpent est sur la pomme
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("apple")
            self.apple.move()
            self.snake.increase_length()

        # on vérifie si le serpent est sur lui même
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("game_over")
                raise "Game Over"

        # on vérifie si le serpent est sur les bords de l'écran
        if not (0 <= self.snake.x[0] < 1000 and 0 <= self.snake.y[0] < 800):
            self.play_sound("game_over")
            raise "Game Over"

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        # on lance la boucle
        running = True
        pause = False
        
        # lorsque la loupe est active
        while running:
            # on recuper les evenements de pygame
            for event in pygame.event.get():
                # losque l'on clique sur une touche ça fais un truc
                if event.type == KEYDOWN:
                    # Losque l'on appuie sur la touche f le jeu se ferme
                    if event.key == K_f or event.key == K_ESCAPE:
                        running = False

                    # Losque l'on appuie sur la touche espace le jeu se met en pause
                    if event.key == K_SPACE or event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        # On fait bouger le serpent avec les touches du clavier
                        if event.key == K_LEFT or event.key == K_q:
                            self.snake.move_left()
                        if event.key == K_RIGHT or event.key == K_d:
                            self.snake.move_right()
                        if event.key == K_UP or event.key == K_z:
                            self.snake.move_up()
                        if event.key == K_DOWN or event.key == K_s:
                            self.snake.move_down()

                # losque l'on appuie sur la touche quitter le jeu se ferme
                elif event.type == QUIT:
                    running = False
            
            try:
                if not pause:
                    # On lance la fonction play
                    self.play()
            except Exception as e:
                # On affiche le message d'erreur
                self.show_game_over()
                pause = True
                self.reset()
                

            # On met un temps d'attente pour que le jeu ne soit pas trop rapide
            time.sleep(0.1)

if __name__ == "__main__":
    game = Game()
    game.run()
