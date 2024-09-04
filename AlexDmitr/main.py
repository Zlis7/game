import pygame as pg


WIN_WIDTH = 1024
WIN_HEIGHT = 768
URL_BACKGROUND = './content/background.jpg'

    
class InitSettings:
    def __init__(self):
        self.__WIN_WIDTH = 1024
        self.__WIN_HEIGHT = 768
        self.__URL_BACKGROUND = './content/background.jpg'
        self.__screen = pg.display.set_mode(
            (self.__WIN_WIDTH, self.__WIN_HEIGHT)
        )
        self.__background_image = pg.transform.scale(
            pg.image.load(self.__URL_BACKGROUND),
            (self.__WIN_WIDTH,self.__WIN_HEIGHT)
        )

def stage_of_readiness(screen):
    font = pg.font.Font(None, 45)
    
    player_1 = False
    player_2 = False
    isPressPlayers = False

    screen.fill((0, 0, 0))
    screen.blit(
        font.render('Оба игрока, нажмите клавиши вверх', True,(255,255,255)),
        (WIN_WIDTH // 4, WIN_HEIGHT // 2)
        )
    pg.display.flip()
    
    seconds_before_start = 5
    
    while True:    
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == 1:
                screen.fill((0, 0, 0))
                screen.blit(
                    font.render(str(seconds_before_start),True,(255,255,255)),
                    (WIN_WIDTH // 2,WIN_HEIGHT // 2)
                    )
                pg.display.flip()
                seconds_before_start -= 1
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_UP:
                    player_1 = True
                if i.key == pg.K_w:
                    player_2 = True
                    
        if player_1 and player_2 and not isPressPlayers:
            pg.time.set_timer(1, 800)
            isPressPlayers = True

        if seconds_before_start <= -1:
            pg.time.set_timer(1, 0)
            break

def stage_of_game(screen):
    COLOR_USER_1 = (100,250,50)
    COLOR_USER_2 = (50,200,200)
    health_user_1 = 100
    health_user_2 = 100
    rect_user_1 = pg.Rect(7,WIN_HEIGHT //1.7,200,300)
    rect_user_2 = pg.Rect(WIN_WIDTH - 207,WIN_HEIGHT //1.7,200,300)

    background_image = pg.transform.scale(pg.image.load(URL_BACKGROUND),(WIN_WIDTH,WIN_HEIGHT))


    # 1 - номер раунда, 2 - время до начала нового боя, 3 - текущее время
    time_keeper = [1, 10, 10]

    pg.time.set_timer(1, time_keeper[1] * 1000)
    pg.time.set_timer(2, 1000)

    round_font = pg.font.Font(None, 60)
    timer_font = pg.font.Font(None, 80)
    
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            elif i.type == 1:
                time_keeper[0] += 1
                time_keeper[1] += 1
                time_keeper[2] = time_keeper[1]
                pg.time.set_timer(1, time_keeper[1] * 1000)
            elif i.type == 2:
                time_keeper[2] -= 1
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_1:
                    health_user_1 -= 1
                if i.key == pg.K_2:
                    pass
                if i.key == pg.K_3:
                   pass
                if i.key == pg.K_KP1:
                    health_user_2 -= 50
                if i.key == pg.K_KP2:
                    health_user_2 -= 1
                if i.key == pg.K_KP3:
                    health_user_2 -= 1

        screen.blit(background_image,(0,0))
        
        user_1 = pg.draw.rect(
            screen,
            COLOR_USER_1,
            rect_user_1,
            health_user_1,
            20
        )
    
        user_2 = pg.draw.rect(
            screen,
            COLOR_USER_2,
            rect_user_2,
            health_user_2,
            20
        )

        screen.blit(
            round_font.render(f'Round {time_keeper[0]}',
            True,
            (0,0,0)),
            (7, 7)
        )
        screen.blit(
            timer_font.render(f'{time_keeper[2]}',
            True,
            (0,0,0)),
            (7, 63)
        )

        pg.display.flip()
        pg.time.delay(20)

def main():
    pg.init()
    
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    #stage_of_readiness(screen)
    stage_of_game(screen)
    
    

if __name__ == '__main__':
    main()
