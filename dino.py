import pygame

pygame.init()
clock = pygame.time.Clock()

#Tạo tiêu đề và icon
pygame.display.set_caption("Dinosaur Game")
icon = pygame.image.load("assets\dinosaur.png")
pygame.display.set_icon(icon)

#Cửa số game
screen = pygame.display.set_mode((600,300))

#Load hình ảnh
bg = pygame.image.load("assets\\background.jpg")
dino = pygame.image.load("assets\dinosaur.png")
tree = pygame.image.load("assets\\tree.png")

#Load âm thanh
sound_over = pygame.mixer.Sound("sound\\te.wav")
sound_play = pygame.mixer.Sound("sound\\tick.wav")

#Khởi tạo tọa độ các đối tượng trong game
bg_x,bg_y = 0,0
dino_x, dino_y = 0,230
tree_x, tree_y = 550, 230
x_def = 5
y_def = 7
jump = False
game_play = True
score = 0

f = open("high_score.txt", "r")
if (f.read() == ""):
    high_score = 0
else:
    f = open("high_score.txt", "r")
    high_score = float(f.read())

def check_collide():
    if dino_hcn.colliderect(tree_hcn):
        pygame.mixer.Sound.play(sound_over)
        return False
    return True

#Vẽ score và high_score
game_font = pygame.font.Font("04B_19.TTF", 20)

def score_view():
    if game_play:
        score_txt = game_font.render(f"Score: {int(score)}", True, (0,0,0))
        screen.blit(score_txt, (250,50))
        high_score_txt = game_font.render(f"High Score: {int(high_score)}", True, (255,0,0))
        screen.blit(high_score_txt, (225,80))
    else: 
        score_txt = game_font.render(f"Score: {int(score)}", True, (0,0,0))
        screen.blit(score_txt, (250,50))
        high_score_txt = game_font.render(f"High Score: {int(high_score)}", True, (255,0,0))
        screen.blit(high_score_txt, (225,80))
        game_over_txt = game_font.render(f"Game Over!", True, (255,0,0))
        screen.blit(game_over_txt, (235,120))

#Vòng lặp xử lý game
running = True

while running:
    #Chỉnh FPS
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_play:
            if event.key == pygame.K_SPACE:
                if dino_y == 230:
                    jump=True
                    pygame.mixer.Sound.play(sound_play)
        if event.type == pygame.KEYDOWN and game_play == False:
            game_play = True
    if game_play: 
        # Vẽ hình   
        #background
        bg_hcn = screen.blit(bg, (bg_x, bg_y))
        bg_x -= x_def
        if bg_x == -10:
            bg_x = 0
        #tree
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        tree_x -= x_def
        if tree_x == -50:
            tree_x = 550 
        #dino
        dino_hcn = screen.blit(dino, (dino_x, dino_y))
        if dino_y >= 80 and jump:
            dino_y -= y_def
        else:
            jump=False
        if dino_y < 230 and jump == False:
            dino_y += y_def
        score += 0.01
        if high_score < score:
            high_score = score
        f = open("high_score.txt", "w+")
        f.write(str(int(high_score)))
        f.close()
        game_play = check_collide()
        score_view()
    else: 
        #Reset Game
        bg_x,bg_y = 0,0
        dino_x, dino_y = 0,230
        tree_x, tree_y = 550, 230
        bg_hcn = screen.blit(bg, (bg_x, bg_y))
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        dino_hcn = screen.blit(dino, (dino_x, dino_y))
        score = 0
        score_view()


    pygame.display.update()
