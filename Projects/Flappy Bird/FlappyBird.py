import pygame
import sys
import random
import os.path
# UI
choice = input("Press 1 for Single Player Mode\nPress 2 for Two-Player Mode\nPress 3 for Highscores")
if choice == '1':
    name = input("Enter Your Name:")
    pygame.init()

    # Random no generator
    def random_no():
        return random.randint(-280, 50)

    def random_no2():
        return random.randint(100, 400)

    #Level UP
    def lvlup():
        global pipe_speed, pipe_space
        pipe_space -= 10
        pipe_speed -= 1

    # Pipes mover
    def PipesMover():
        global enemy_rect
        for j in range(3):
            pipe_rect_up[j] = pipe_rect_up[j].move((pipe_speed, 0))
            pipe_rect_down[j] = pipe_rect_down[j].move((pipe_speed, 0))

        enemy_rect = enemy_rect.move((pipe_speed, enemy_y_switch))


    # pipes printer
    def PipesPrinter():
        for k in range(3):
            screen.blit(pipe_surface_up[k], pipe_rect_up[k])
            screen.blit(pygame.transform.flip(pipe_surface_down[k], False, True), pipe_rect_down[k])

        screen.blit(enemy, enemy_rect)

    # pipes regenrator
    def PipesRegenerator():
        global enemy_rect, flag
        for l in range(3):
            if pipe_rect_up[l].right < 0:
                pipe_y = random_no()
                pipe_rect_up[l] = pipe_surface_up[l].get_rect(center=(1290, pipe_y))
                pipe_rect_down[l] = pipe_surface_down[l].get_rect(center=(1290, pipe_y + pipe_space))
                if(random.randint(0, 4) == 1) and flag != 0:
                    flag = 0
                    enemy_rect = enemy.get_rect(center=(pipe_rect_down[l].x + 250, random_no2()))

        if enemy_rect.right < 0:
            enemy_rect = enemy.get_rect(center=(1000, -100))
            flag = 1

    # Collison Detector
    def CollisonDetector():

        for m in range(3):
            if ball_rect.colliderect(pipe_rect_up[m]):
                return 1
            if ball_rect.colliderect(pipe_rect_down[m]):
                return 1
        if ball_rect.bottom >= 620 or ball_rect.top <= 0:
            return 1

        if ball_rect.colliderect(enemy_rect):
            return 1

    # Score Text
    def ScoreDisplay():
        font_score = pygame.font.Font(None, 40)
        ren_score = font_score.render(str(int(score)), 0, white)
        screen.blit(ren_score, (638, 50))

    # Game Over Text
    def GameOver():
        font = pygame.font.Font(None, 80)
        ren = font.render(text, 0, black)
        screen.blit(ren, (400, 300))

    # Writing Highscores
    def Highscore_write():
        highscore_file = open("Highscores.txt", "a")
        highscore_file.write("\n" + name + " " + str(int(score)))
        highscore_file.close()

    # Writing individual Highscores
    def Highscore_indiv():
        ind_highscore_file = open(name + ".txt", "a")
        ind_highscore_file.write(" " + str(int(score)))
        ind_highscore_file.close()

    # colors
    black = (0, 0, 0)
    red = (255, 26, 79)
    white = (255, 255, 255)
    ground_colour = (230, 209, 125)
    green = (0, 145, 15)
    blue = (18, 161, 255)
    sky_blue = (164, 238, 255)

    # co-ordinate and other variables
    speed = 0
    gravity = 0.25
    frame = 0
    frame_speed = 0.1
    score = 0
    lvlup_counter = 0
    pipe_space = 850
    pipe_speed = -5
    enemy_y = 0
    enemy_y_switch = 2
    flag = 1
    # clock
    clock = pygame.time.Clock()

    # screen
    screen = pygame.display.set_mode((1280, 720))
    bg_surface = pygame.image.load('Assets/bg1.png').convert()

    # ball
    ball_surface1 = pygame.image.load('Assets/Bird Animation 1/bird0.png').convert_alpha()
    ball_surface2 = pygame.image.load('Assets/Bird Animation 1/bird1.png').convert_alpha()
    ball_surface3 = pygame.image.load('Assets/Bird Animation 1/bird2.png').convert_alpha()
    ball_surface = [ball_surface1, ball_surface2, ball_surface3]

    # ball_surface.fill(sky_blue)
    # ball_surface[0] = pygame.transform.scale(ball_surface[0], (41, 30))
    # ball_surface[1] = pygame.transform.scale(ball_surface[1], (41, 30))
    # ball_surface[2] = pygame.transform.scale(ball_surface[2], (41, 30))
    ball_rect = ball_surface[0].get_rect(center=(500, 100))

    # ground surface
    ground_surface = pygame.image.load('Assets/ground1.png').convert()
    ground_surface1 = pygame.image.load('Assets/ground1.png').convert()
    ground_rect = ground_surface.get_rect(bottomleft=(0, 720))

    # obstacle
    enemy = pygame.image.load('Assets/enemy.png').convert_alpha()
    enemy_rect = enemy.get_rect(center=(1000, -100))

    # pipe surface
    pipe_surface_up = []
    pipe_surface_down = []
    pipe_rect_up = []
    pipe_rect_down = []
    for i in range(3):
        pipe_surface_up.append(pygame.image.load('Assets/Pipe.png').convert())
        pipe_surface_down.append(pygame.image.load('Assets/Pipe.png').convert())
        pipey = random_no()
        pipe_rect_up.append(pipe_surface_up[i].get_rect(center=(1000 + i * 432, pipey)))
        pipe_rect_down.append(pipe_surface_down[i].get_rect(center=(1000 + i * 432, pipey + pipe_space)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                speed = -10

        speed = speed + gravity
        frame = frame + frame_speed
        score = score + 0.01
        lvlup_counter = lvlup_counter + 1
        enemy_y = enemy_y + enemy_y_switch
        if enemy_y == 40:
            enemy_y_switch = -2
        if enemy_y == -40:
            enemy_y_switch = 2
        if int(frame) > 2:
            frame = 0
        ball_rect = ball_rect.move((0, int(speed)))
        if ground_rect.right <= 0:
            ground_rect.left = 0
        if lvlup_counter > 2000:
            lvlup_counter = 0
            lvlup()
        ground_rect = ground_rect.move(pipe_speed, 0)
        PipesMover()
        PipesRegenerator()
        screen.fill(white)
        screen.blit(bg_surface, (0, 0))
        screen.blit(ball_surface[int(frame)], ball_rect)
        PipesPrinter()
        screen.blit(ground_surface, ground_rect)
        screen.blit(ground_surface, (ground_rect.right, 620))
        ScoreDisplay()
        pygame.display.flip()
        if CollisonDetector():
            text = "Game Over " + name
            GameOver()
            Highscore_write()
            Highscore_indiv()
            pygame.display.flip()
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()
        clock.tick(60)

elif choice == '2':
    name1 = input("Enter the name of Player 1:")
    name2 = input("Enter the name of Player 2:")

    pygame.init()

    # Random no generator
    def random_no():
        return random.randint(-280, 50)

    def lvlup():
        global pipe_speed, pipe_space
        pipe_space -= 10
        pipe_speed -= 1

    # Pipes mover
    def PipesMover():
        for j in range(3):
            pipe_rect_up[j] = pipe_rect_up[j].move((pipe_speed, 0))
            pipe_rect_down[j] = pipe_rect_down[j].move((pipe_speed, 0))


    # pipes printer
    def PipesPrinter():
        for k in range(3):
            screen.blit(pipe_surface_up[k], pipe_rect_up[k])
            screen.blit(pygame.transform.flip(pipe_surface_down[k], False, True), pipe_rect_down[k])


    # pipes re-generator
    def PipesRegenerator():
        for l in range(3):
            if pipe_rect_up[l].right < 0:
                pipe_y = random_no()
                pipe_rect_up[l] = pipe_surface_up[l].get_rect(center=(1290, pipe_y))
                pipe_rect_down[l] = pipe_surface_down[l].get_rect(center=(1290, pipe_y + pipe_space))


    # Collision Detector
    def CollisionDetector():
        for m in range(3):
            if ball_rect.colliderect(pipe_rect_up[m]):
                return 1
            if ball_rect.colliderect(pipe_rect_down[m]):
                return 1
            if ball2_rect.colliderect(pipe_rect_up[m]):
                return 2
            if ball2_rect.colliderect(pipe_rect_down[m]):
                return 2
        if ball_rect.bottom >= 620 or ball_rect.top <= 0:
            return 1
        if ball2_rect.bottom >= 620 or ball2_rect.top <= 0:
            return 2


    # Game Over Text
    def GameOver():
        font = pygame.font.Font(None, 80)
        ren = font.render(text, 0, black)
        screen.blit(ren, (500, 300))


    # colors
    black = (0, 0, 0)
    red = (255, 26, 79)
    white = (255, 255, 255)
    ground_colour = (230, 209, 125)
    green = (0, 145, 15)
    blue = (18, 161, 255)
    sky_blue = (164, 238, 255)

    # text

    text = ""

    # co-ordinate variables
    speed1 = 0
    speed2 = 0
    gravity = 0.25
    frame = 0
    frame_speed = 0.2
    lvlup_counter = 0
    pipe_space = 850
    pipe_speed = -5

    # clock
    clock = pygame.time.Clock()

    # screen
    screen = pygame.display.set_mode((1280, 720))
    bg_surface = pygame.image.load('Assets/bg1.png').convert()

    # ball
    ball_surface1 = pygame.image.load('Assets/bird3.png').convert_alpha()
    ball_surface2 = pygame.image.load('Assets/bird3.png').convert_alpha()
    ball_surface3 = pygame.image.load('Assets/bird3.png').convert_alpha()

    ball_surface = [ball_surface1, ball_surface2, ball_surface3]
    ball_surface[0] = pygame.transform.scale(ball_surface[0], (41, 30))
    ball_surface[1] = pygame.transform.scale(ball_surface[1], (41, 30))
    ball_surface[2] = pygame.transform.scale(ball_surface[2], (41, 30))
    ball_rect = ball_surface[0].get_rect(center=(500, 100))

    # ball2
    ball2_surface1 = pygame.image.load('Assets/bird2.png').convert_alpha()
    ball2_surface2 = pygame.image.load('Assets/bird2.png').convert_alpha()
    ball2_surface3 = pygame.image.load('Assets/bird2.png').convert_alpha()

    ball2_surface = [ball2_surface1, ball2_surface2, ball2_surface3]
    ball2_surface[0] = pygame.transform.scale(ball2_surface[0], (41, 30))
    ball2_surface[1] = pygame.transform.scale(ball2_surface[1], (41, 30))
    ball2_surface[2] = pygame.transform.scale(ball2_surface[2], (41, 30))
    ball2_rect = ball_surface[0].get_rect(center=(400, 100))

    # ground surface
    ground_surface = pygame.image.load('Assets/ground1.png').convert()
    ground_surface1 = pygame.image.load('Assets/ground1.png').convert()
    ground_rect = ground_surface.get_rect(bottomleft=(0, 720))

    # pipe surface
    pipe_surface_up = []
    pipe_surface_down = []
    pipe_rect_up = []
    pipe_rect_down = []
    for i in range(3):
        print(i)
        pipe_surface_up.append(pygame.image.load('Assets/Pipe.png').convert())
        pipe_surface_down.append(pygame.image.load('Assets/Pipe.png').convert())
        pipey = random_no()
        pipe_rect_up.append(pipe_surface_up[i].get_rect(center=(1000 + i * 432, pipey)))
        pipe_rect_down.append(pipe_surface_down[i].get_rect(center=(1000 + i * 432, pipey + pipe_space)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed1 = -10

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    speed2 = -10

        speed1 = speed1 + gravity
        speed2 = speed2 + gravity
        frame = frame + frame_speed

        if lvlup_counter > 2000:
            lvlup_counter = 0
            lvlup()
        if int(frame) > 2:
            frame = 0
        ball_rect = ball_rect.move((0, int(speed1)))
        ball2_rect = ball2_rect.move((0, int(speed2)))
        if ground_rect.right <= 0:
            ground_rect.left = 0
        ground_rect = ground_rect.move(pipe_speed, 0)
        PipesMover()
        PipesRegenerator()
        screen.fill(white)
        screen.blit(bg_surface, (0, 0))
        screen.blit(ball_surface[int(frame)], ball_rect)
        screen.blit(ball2_surface[int(frame)], ball2_rect)
        PipesPrinter()
        screen.blit(ground_surface, ground_rect)
        screen.blit(ground_surface, (ground_rect.right, 620))
        pygame.display.flip()
        if CollisionDetector():
            if CollisionDetector() == 1:
                text = name2 + " won"
            elif CollisionDetector() == 2:
                text = name1 + " won"
            GameOver()
            pygame.display.flip()
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()

        clock.tick(60)

elif choice == '3':
    print("\n1.Global Highscores \n2.Individual Highscores")
    ch = int(input())
    if ch == 1:
        def Sorting_scores(e):
            return e[0]

        def Sorting_scores2(e):
            return int(e[1])

        highscore_file = open("Highscores.txt", "r+")
        index = 0
        scores = []
        for i in highscore_file.readlines():
            scores.append(i.split())
            index = index + 1

        index = 0
        scores.sort(key=Sorting_scores)
        length_scores = len(scores)-1
        while index < length_scores:
            if scores[index][0] == scores[index+1][0]:
                length_scores = length_scores - 1
                if int(scores[index][1]) >= int(scores[index + 1][1]):
                    scores.pop(index+1)
                else:
                    scores.pop(index)
            else:
                index = index+1
        scores.sort(reverse=True, key=Sorting_scores2)
        print("\n-----------------------HighScores-----------------------")
        for index in scores:
            print(index[0] + " - " + index[1])
        input("\nPress any key to exit")
    elif ch == 2:
        print("Enter Your Name:")
        name = input()
        if os.path.isfile(name + ".txt"):
            ind_highscore_file = open(name + ".txt", "r+")
            for i in ind_highscore_file.readlines():
                scores = i.split()

            scores.sort(reverse=True)
            print("\n-----------------------HighScores-----------------------")
            for i in scores:
                print(i)
        else:
            print("\nSorry, You do not have any highscores")
        input("\nPress any key to exit")


