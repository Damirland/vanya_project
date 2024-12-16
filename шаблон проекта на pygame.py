import pygame as pg

from sprites import *

pg.mixer.init()

size = (500, 500)
screen = pg.display.set_mode(size)

fps = 100
clock = pg.time.Clock()

background = pg.image.load("Фон для игры на pygame.png")
background = pg.transform.scale(background, size)

character = Character()

star = pg.sprite.Group()
star.add(Star())
star.add(Star())
star.add(Star())
star.add(Star())
star.add(Star())
star.add(Star())
star.add(Star())
star.add(Star())
star.add(Star())


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    character.update()
    star.update()

    screen.blit(background, (0, 0))
    screen.blit(character.image, character.rect)
    star.draw(screen)

    pg.display.flip()
    clock.tick(fps)
