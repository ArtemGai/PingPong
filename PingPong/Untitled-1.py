from pygame import *
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('bigbob.png'), (win_width, win_height))

window.blit(background,(0,0))

game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))   
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width -80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width -80:
            self.rect.y += self.speed

racket1 = Player("bigbobitaly.png", 30, 100, 30, 150, 15)
racket2 = Player("bigbobfis.png", 520, 100, 30, 150, 15)
        

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True:

            window.blit(background,(0,0))

            racket1.update_l()
            racket2.update_r()

            racket1.reset()
            racket2.reset()


    display.update()
    clock.tick(FPS)
