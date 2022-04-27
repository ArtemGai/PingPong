from pygame import *
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('bigbob.png'), (win_width, win_height))

window.blit(background,(0,0))

game = True
finish = False
clock = time.Clock()
FPS = 120



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
ball = GameSprite('bigbobcheese.png', 280, 200, 40, 40, 4)


font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 Lose!', 180, (180, 0, 0))
lose2 = font.render('Player 2 Lose!', 180, (180, 0, 0))

dx = 3
dy = 3

score_left = 0
score_right = 0


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background,(0,0))

        racket1.update_l()
        racket2.update_r()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        ball.rect.x += dx #движение мяча
        ball.rect.y += dy #движение мяча

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            dx *= - 1
        if ball.rect.y < 0 or ball.rect.y > win_height-40:
            dy *= - 1

        score_l = font.render(str(score_left), True, (255,255,255))
        score_r = font.render(str(score_right), True, (255,255,255))
        window.blit(score_l, (10, 10))
        window.blit(score_r, (win_width-25, 10))

        if ball.rect.x < 0:
            score_right += 1
            ball.rect.x = 280
            ball.rect.y = 200

        if ball.rect.x > win_width:
            score_left += 1
            ball.rect.x = 280
            ball.rect.y = 200
        
        racket1.reset()
        racket2.reset()

        ball.reset()
                
    display.update()
    clock.tick(FPS)
