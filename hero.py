import pygame
from sys import exit
#Stworzenie klasy CapMan
class CapMan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Ilość serduszek
        self.hearts = 2
        #Prędkość z jaką Cap-Man będzie się poruszał (pixels per frame)
        self.speed = 2
        #Pomocniczy obrazek, do zmiany
        self.image = pygame.image.load('../zdj/cap_man_1.png').convert_alpha()
        #Podstawowa pozycja Cap - Mana
        self.rect = self.image.get_rect(center = (200,500))
    #def player_input(self):
        #Funkcja poruszania się Cap - Mana po wciśnięciu odpowiednich klawiszy, obecnie niepotrzebna
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     self.rect.y -= self.speed
        # elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     self.rect.y += self.speed
        # elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #     self.rect.x += self.speed
        # elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #     self.rect.x -= self.speed
    def player_movement(self, pressed_key):
        #Porusza się w odpowiednim kierunku pod warunkiem że środek jest na ekranie
        #Oraz nie zostanie wciśnięty inny klawisz
        if (pressed_key == pygame.K_UP or pressed_key == pygame.K_w) and self.rect.centery > 0:
            self.rect.y -= self.speed
        elif (pressed_key == pygame.K_DOWN or pressed_key == pygame.K_s) and self.rect.centery < 680:
            self.rect.y += self.speed
        elif (pressed_key == pygame.K_RIGHT or pressed_key == pygame.K_d) and self.rect.centerx > 0:
            self.rect.x += self.speed
        elif (pressed_key == pygame.K_LEFT or pressed_key == pygame.K_a) and self.rect.centerx < 920:
            self.rect.x -= self.speed
    @staticmethod
    def checking_Pressed_Keys():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            return pygame.K_UP
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            return pygame.K_DOWN
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            return pygame.K_RIGHT
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            return pygame.K_LEFT
        return None
    def update(self,pressed_key):
        self.player_movement(pressed_key)

        
pygame.init()

screen = pygame.display.set_mode((920,680))
clock = pygame.time.Clock()
running = True
pressed_key = None
#Stworzenie naszej postaci, przed główną pętlą gry
player = pygame.sprite.GroupSingle()
player.add(CapMan())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            last_key = player.sprite.checking_Pressed_Keys()
            if last_key != None:
                pressed_key = last_key
    screen.fill("Purple")
    #Narysowanie Cap-Mana na ekranie
    player.draw(screen)
    #Aktualizuje co robimy z naszą postacią
    player.update(pressed_key)
    #
    pygame.display.flip()
    #Testowe odwołanie się do zmiennej hearts oraz zmiana jej wartości
    # player.sprite.hearts -= 1
    # print(player.sprite.hearts)
    clock.tick(60)
pygame.quit()