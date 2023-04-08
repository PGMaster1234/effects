#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
from pygame.locals import *
import math
import pygame
import random
import sys

# Setup pygame/window ---------------------------------------- #
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('explosions')
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE, 32)
screen2 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()
screen3 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()
screen4 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()
screen5 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()
particles = []


class Particles:
    def __init__(self, loc0, loc1, movement, color, size, type):
        self.type = type
        self.loc0 = loc0
        self.loc1 = loc1
        self.movement = movement
        self.color = color
        self.size = size
        self.alive = True

    def move(self):
        self.loc0 += self.movement[0]
        self.loc1 += self.movement[1]
        if self.type == 0:
            if (500/self.size) > 1:
                self.size += int(500/self.size)
            else:
                if 100 < random.randint(1, int(1000 * (500/self.size))):
                    self.size += int(500/self.size)
        else:
            self.size -= (((self.size + 10)/400) + random.uniform(-0.05, 0.05) + 0.05)
            if self.size < 0:
                self.alive = False
            if self.size > 800:
                self.alive = False

    def draw(self, screen, screen2, screen3, screen4, screen5):
        if self.type == 0:
            pygame.draw.circle(screen, self.color, (self.loc0, self.loc1), self.size, int(1000/self.size) + 1)
        if self.type == 1:
            pygame.draw.circle(screen2, self.color, (self.loc0, self.loc1), self.size)
        if self.type == 2:
            pygame.draw.circle(screen3, self.color, (self.loc0, self.loc1), self.size)
        if self.type == 3:
            pygame.draw.circle(screen4, self.color, (self.loc0, self.loc1), self.size)
        if self.type == 4:
            pygame.draw.circle(screen5, self.color, (self.loc0, self.loc1), self.size)


def explosion(pos0, pos1):
    if stopper < 3:
        particles.append(Particles(pos0, pos1, [0, 0], (235, 237, 233), random.randint(5, 10), 0))
    for i in range(60):
        pos0 += random.randint(-5, 5)
        pos1 += random.randint(-5, 5)
        a = random.randint(0, 89)
        if a < 10:
            particles.append(Particles(pos0, pos1, [random.uniform(-1, 1), random.uniform(1, -2)],
                                       (218, 134, 62, 240), random.randint(25, 30), random.randint(2, 3)))
        if 9 < a < 20:
            particles.append(Particles(pos0, pos1, [random.uniform(-1, 1), random.uniform(1, -2)],
                                       (235, 237, 233, 240), random.randint(25, 30), random.randint(2, 3)))
        if 19 < a < 30:
            particles.append(Particles(pos0, pos1, [random.uniform(-1, 1), random.uniform(1, -2)],
                                       (117, 36, 56, 240), random.randint(30, 35), random.randint(2, 3)))
        if 29 < a < 40:
            pass
        if 39 < a < 45:
            particles.append(Particles(pos0, pos1, [random.uniform(-1, 1), random.uniform(1, -2)],
                                       (232, 193, 112, 240), random.randint(10, 15), random.randint(3, 4)))
        if 44 < a < 50:
            particles.append(Particles(pos0, pos1, [random.uniform(-1, 1), random.uniform(1, -2)],
                                       (36, 21, 39, 240), random.randint(10, 15), random.randint(3, 4)))
        if 54 < a < 60:
            particles.append(Particles(pos0, pos1, [random.uniform(-1, 1), random.uniform(0.5, -4)],
                                       (21, 29, 40, 240), random.randint(10, 15), random.randint(3, 4)))
        if 64 < a < 90:
            particles.append(Particles(pos0, pos1, [random.uniform(-0.5, 0.5), random.uniform(0.5, -3)],
                                       (21, 29, 40, 240), random.randint(50, 55), random.randint(1, 2)))


tick = 400
stopper = 0
# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((79, 143, 186))
    screen.blit(screen2, (0, 0))
    screen.blit(screen3, (0, 0))
    screen.blit(screen4, (0, 0))
    screen.blit(screen5, (0, 0))
    screen2 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()
    screen3 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()
    screen4 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()
    screen5 = pygame.Surface((screen.get_width(), screen.get_height())).convert_alpha()

    for i, particle in sorted(enumerate(particles), reverse=True):
        particle.move()
        particle.draw(screen, screen2, screen3, screen4, screen5)

        if not particle.alive:
            particles.pop(i)

    mx, my = pygame.mouse.get_pos()

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    tick += 1
    if tick > 500:
        if stopper < 5:
            stopper += 1
            explosion(screen.get_width()/2, 3*screen.get_height()/5)
            tick = 490
        else:
            stopper = 0
            tick = 0

    # Update ------------------------------------------------- #
    pygame.display.update()
    clock.tick(60)
