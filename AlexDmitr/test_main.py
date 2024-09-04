import pygame as pg

pg.init()

screen = pg.display.set_mode((1024, 768))
background_image = pg.transform.scale(pg.image.load('./content/background.jpg'),(1024,768))
screen.blit(background_image,(0,0))
pg.display.flip()

ox_1 = 40
ox_2 = 1024 - 124
oy_1 = 40
oy_2 = 40

max_columns_armies = 2
rect_list_1 = [[] for i in range(max_columns_armies)]
rect_list_2 = [[] for i in range(max_columns_armies)]

#rect_list_1 = [list(reversed(x)) for x in rect_list_1]

font = pg.font.Font(None, 45)

pg.display.flip()

stop_run = False
time_fight = False

str_1 = 0
str_2 = 0

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pass
        elif i.type == 1:
            pass
        elif i.type == pg.KEYDOWN and not time_fight:
                if i.key == pg.K_0:
                    time_fight = True

                if i.key == pg.K_1:
                    rect_list_1[str_1].append(pg.Rect(ox_1, oy_1, 20, 20))
                    ox_1 += 30
                if i.key == pg.K_2:
                    rect_list_1[str_1].append(pg.Rect(ox_1, oy_1, 35, 35))
                    ox_1 += 30
                if i.key == pg.K_3:
                    rect_list_1[str_1].append(pg.Rect(ox_1, oy_1, 50, 50))
                if i.key == pg.K_4 and str_1 < max_columns_armies - 1:
                    str_1 += 1
                if i.key == pg.K_5 and str_1 > 0:
                    str_1 -= 1
                if i.key == pg.K_KP1:
                    rect_list_2[str_2].append(pg.Rect(ox_2, oy_2, 20, 20))

                if i.key == pg.K_KP2:
                    rect_list_2[str_2].append(pg.Rect(ox_2, oy_2, 35, 35))
                if i.key == pg.K_KP3:
                    rect_list_2[str_2].append(pg.Rect(ox_2, oy_2, 50, 50))

                if i.key == pg.K_KP4 and str_2 < max_columns_armies - 1:
                    str_2 += 1
                if i.key == pg.K_KP5 and str_2 > 0:
                    str_2 -= 1
                
    screen.blit(background_image,(0,0))

    if time_fight:
        for array in rect_list_1:
            for elem in array:
                elem.move_ip(20, 0)

                if elem.width == 35:
                    pg.draw.rect(screen, (200, 180, 0), elem)
                elif elem.width > 35:
                    pg.draw.rect(screen, (200, 200, 0), elem)
                else:
                    pg.draw.rect(screen, (180, 180, 180), elem)
                pg.display.flip()
        for x in rect_list_2:
            for elem in array:
                elem.move_ip(-20, 0)

                if elem.width == 35:
                    pg.draw.rect(screen, (200, 180, 0), elem)
                elif elem.width > 35:
                    pg.draw.rect(screen, (200, 200, 0), elem)
                else:
                    pg.draw.rect(screen, (180, 180, 180), elem)
                pg.display.flip()

    screen.blit(
        font.render(f'{str_1} / {str_2}', True,(255,255,255)),
        (1024 // 4, 768 // 2)
        )

    pg.display.flip()

    if time_fight:
        pg.time.delay(1200)
    else:
        pg.time.delay(20)





