import sys, pygame, random, time#импортировать все библиотеки

pygame.init()#initialization
WINDOWWIDTH = 800#parameters of window
WINDOWHEIGHT = 512
FPS = 30

CARWIDTH = WINDOWWIDTH / 9#parameters of a car
CARHEIGHT = WINDOWHEIGHT / 4
RECTWIDTH = WINDOWWIDTH / 20#storing rect areas
RECTHEIGHT = WINDOWHEIGHT / 40
COINSIZE = WINDOWWIDTH / 16
YDIFF = WINDOWHEIGHT / 8

STEP = 5

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()#for controlling fps
DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))#displaying

car = pygame.image.load('images/car.png')#downloading the images
road = pygame.image.load('images/road2.png')
coin = pygame.image.load('images/coin.jpeg')
inc = pygame.image.load('images/car_2.png')

point_sound = pygame.mixer.Sound('music/car.wav')#background music

smallfont = pygame.font.Font(None, 28)#шрифты
menufont = pygame.font.Font(None, 48)
overfont = pygame.font.Font(None, 60)

pygame.display.set_caption("CAR GAME")#game caption


def gameloop():#starting the game
    startmenu()
    points = 0
    RECTX, RECTY = WINDOWWIDTH / 2, 0
    CARX, CARY = WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + CARHEIGHT
    COINX, COINY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0
    INCX, INCY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0

    direction = -1  # -1 is left,1 is right
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = -1
                elif event.key == pygame.K_RIGHT:
                    direction = 1
                elif event.key == pygame.K_UP:
                    direction = 0
                elif event.key == pygame.K_ESCAPE:
                    pause()
        if direction == -1:
            CARX -= STEP
        elif direction == 1:
            CARX += STEP
        DISPLAY.fill(white)
        DISPLAY.blit(road, (0, 0))
        if (check_coin(CARX, CARY, COINX, COINY)):
            COINX, COINY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0
            points += 1

        RECTY += STEP
        RECTY = RECTY % YDIFF
        COINY += STEP
        INCY += 2 * STEP

        if COINY >= WINDOWHEIGHT:
            COINX, COINY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0
        if INCY >= WINDOWHEIGHT:
            INCX, INCY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0

        for i in range(-1, 8):
            pygame.draw.rect(DISPLAY, black, [RECTX, RECTY + i * YDIFF, RECTWIDTH, RECTHEIGHT])
        DISPLAY.blit(coin, (COINX, COINY))
        DISPLAY.blit(car, (CARX, CARY))

        DISPLAY.blit(inc, (INCX, INCY))

        text = smallfont.render('Score: ' + str(points), True, black)
        DISPLAY.blit(text, (0, 0))

        car_crash(CARX, CARY, INCX, INCY)
        if check_step_out(CARX):
            if CARX < 0.1 * WINDOWWIDTH:
                for i in range(0, 20):
                    DISPLAY.fill(white)
                    DISPLAY.blit(road, (0, 0))
                    if (check_coin(CARX, CARY, COINX, COINY)):
                        COINX, COINY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0
                        points += 1

                    RECTY += STEP
                    RECTY = RECTY % YDIFF
                    COINY += STEP
                    INCY += 2 * STEP
                    CARX -= STEP
                    CARY -= STEP

                    if COINY >= WINDOWHEIGHT:
                        COINX, COINY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0
                    if INCY >= WINDOWHEIGHT:
                        INCX, INCY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0

                    new_car = pygame.transform.rotate(car, 10 + 3 * i)

                    for i in range(-1, 8):
                        pygame.draw.rect(DISPLAY, black, [RECTX, RECTY + i * YDIFF, RECTWIDTH, RECTHEIGHT])
                    DISPLAY.blit(coin, (COINX, COINY))
                    DISPLAY.blit(new_car, (CARX, CARY))

                    DISPLAY.blit(inc, (INCX, INCY))

                    text = smallfont.render('Score: ' + str(points), True, black)
                    DISPLAY.blit(text, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
            if CARX > 0.78 * WINDOWWIDTH:
                for i in range(0, 20):
                    DISPLAY.fill(white)
                    DISPLAY.blit(road, (0, 0))
                    if (check_coin(CARX, CARY, COINX, COINY)):
                        COINX, COINY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0
                        points += 1

                    RECTY += STEP
                    RECTY = RECTY % YDIFF
                    COINY += STEP
                    INCY += 2 * STEP
                    CARX += STEP
                    CARY -= STEP

                    if COINY >= WINDOWHEIGHT:
                        COINX, COINY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0
                    if INCY >= WINDOWHEIGHT:
                        INCX, INCY = random.randrange(0.2 * WINDOWWIDTH, 0.8 * WINDOWWIDTH, STEP), 0

                    new_car = pygame.transform.rotate(car, -(10 + 3 * i))

                    for i in range(-1, 8):
                        pygame.draw.rect(DISPLAY, black, [RECTX, RECTY + i * YDIFF, RECTWIDTH, RECTHEIGHT])
                    DISPLAY.blit(coin, (COINX, COINY))
                    DISPLAY.blit(new_car, (CARX, CARY))

                    DISPLAY.blit(inc, (INCX, INCY))

                    text = smallfont.render('Score: ' + str(points), True, black)
                    DISPLAY.blit(text, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
            game_over()

        clock.tick(FPS)
        pygame.display.update()


def check_coin(CARX, CARY, COINX, COINY):
    if (CARX - COINX) <= COINSIZE and (COINX - CARX) <= CARWIDTH:
        if (CARY - COINY) <= COINSIZE and (COINY - CARY) <= CARHEIGHT:
            point_sound.play()
            return True


def car_crash(CARX, CARY, INCX, INCY):
    if (CARX - INCX) <= CARWIDTH and (INCX - CARX) <= CARWIDTH:
        if (CARY - INCY) <= CARHEIGHT and (INCY - CARY) <= CARHEIGHT:
            game_over()


def startmenu():
    point = 0
    while 1:
        DISPLAY.fill(white)
        if point == 0:
            start = menufont.render('START GAME', True, red)
            quit = menufont.render('QUIT GAME', True, black)
        elif point == 1:
            start = menufont.render('START GAME', True, black)
            quit = menufont.render('QUIT GAME', True, red)
        DISPLAY.blit(start, (WINDOWWIDTH / 10, WINDOWHEIGHT / 10))
        DISPLAY.blit(quit, (WINDOWWIDTH / 10, 3 * WINDOWHEIGHT / 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    point += 1
                elif event.key == pygame.K_UP:
                    point -= 1
                elif event.key == pygame.K_RETURN:
                    if point == 0:
                        return True
                    elif point == 1:
                        pygame.quit()
                        sys.exit()

        point = point % 2
        clock.tick(FPS)
        pygame.display.update()


def game_over():
    DISPLAY.fill(red)
    crashed = overfont.render('YOU CRASHED', True, black)
    gameover = overfont.render('GAME OVER', True, black)
    DISPLAY.blit(crashed, (WINDOWWIDTH / 10, WINDOWHEIGHT / 10))
    DISPLAY.blit(gameover, (WINDOWWIDTH / 10, 5 * WINDOWHEIGHT / 10))
    pygame.display.update()
    time.sleep(2)
    gameloop()


def pause():
    pause = overfont.render('PAUSED', True, red)
    DISPLAY.blit(pause, (0.4 * WINDOWWIDTH, WINDOWHEIGHT / 3))
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return


def check_step_out(CARX):
    if CARX < 0.1 * WINDOWWIDTH or CARX > 0.78 * WINDOWWIDTH:
        return True
    return False


gameloop()