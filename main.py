import pygame
import random
import math
pygame.init()

# ------------------------------ BASIC STUFF

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()
font12 = pygame.font.Font("freesansbold.ttf", 12)
screen2 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screen3 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screen3.set_alpha(100)
fps = 60
clock = pygame.time.Clock()
click = False

# ------------------------------ Variables

shaking = False
shake_amount = 10
pulse_amount = 10
pulse_speed = 0.05
circle_width = 50
x = 0
screenX = 0
screenY = 0
moving_right = False
moving_left = False
moving_up = False
moving_down = False

particles = []
bouncyBALLZ = []
num_ofBALLZ = 200
hasBALLZ = True
dusty = []
triangles = []
distance_for_line = 205
num_of_triangles = 75
speed = 1.5
for i in range(num_of_triangles):
    triangles.append([[random.randint(0, screen_width), random.randint(0, screen_height)],
                      random.uniform(-speed, speed),
                      random.uniform(-speed, speed), random.randint(2, 5)])


class Sparks:
    def __init__(self):
        pass


#
#
#
#
#
#
#
#
#
# ------------------------------ CONTROL CENTER


movement_toggle = True
triangles_toggle = True
dust_toggle = True
bouncyBALLZ_toggle = True
pulsingLight_toggle = True
fire_toggle = True
explosions_toggle = True


# ------------------------------ MAIN LOOP
#
#
#
#
#
#
#
#
running = True
while running:
    mx, my = pygame.mouse.get_pos()

    screen.fill((50, 50, 50))
    screen2.fill((50, 50, 50))

    triangles.append([[mx, my], random.uniform(-1, 1),
                      random.uniform(-1, 1), 7])

    # ------------------------------ User Inputs

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_f:
                shaking = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_f:
                shaking = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

    # ------------------------------ Movement stuff

    if movement_toggle:
        if moving_right:
            screenX += 1
        if moving_left:
            screenX -= 1
        if moving_down:
            screenY += 1
        if moving_up:
            screenY -= 1

    # ------------------------------ Triangles

    if triangles_toggle:
        for tri in triangles:
            if tri[3] < 6:
                pygame.draw.circle(screen2, (255, 255, 255), (tri[0][0], tri[0][1]), tri[3])
            tri[0][0] += tri[1]
            tri[0][1] += tri[2]
            if tri[0][0] > screen_width:
                tri[0][0] = 0
            if tri[0][0] < 0:
                tri[0][0] = screen_width
            if tri[0][1] > screen_height:
                tri[0][1] = 0
            if tri[0][1] < 0:
                tri[0][1] = screen_height

            for t in triangles:
                d = math.sqrt(math.pow((math.fabs(t[0][0] - tri[0][0])), 2) + math.pow((math.fabs(t[0][1]
                                                                                                  - tri[0][1])), 2))
                distance_for_line = tri[3] * 40
                if distance_for_line > d > 0:
                    thicc = int((tri[3]/2 + 100/d)*2/5)
                    if thicc > 7:
                        thicc = 7
                    color = int(math.pow((-d/2 + 255), 2) * 1 / 250)
                    if color > 250:
                        color = 255
                    if color < 50:
                        color = 50
                    pygame.draw.line(screen2, (color, color, color), (tri[0][0], tri[0][1]), (t[0][0], t[0][1]), thicc)

        triangles.remove(triangles[-1])
    # ------------------------------ Dust? idk

    if dust_toggle:
        for i in range(2):
            dusty.append([[900, 200], random.uniform(-1, 1), random.uniform(-0.2, -1.0), 3, 0])

        for dust in dusty:
            pygame.draw.circle(screen2, (222, 177, 132), (dust[0][0], dust[0][1]), dust[3])
            dust[3] -= random.uniform(0.005, 0.01)
            dust[0][0] += dust[1]
            dust[0][1] += dust[2]
            dust[2] += 0.01
            dust[1] *= 0.99
            dust[4] += 1
            dust[1] += random.uniform(-0.1, 0.1)
            dust[2] += random.uniform(-0.1, 0.1)
            if dust[4] > 150:
                dusty.remove(dust)
            if dust[0][1] > screen_height:
                dust[2] /= -2
                dust[0][1] = (screen_height - dust[3])

    # ------------------------------ BouncyBALLZ

    if bouncyBALLZ_toggle:
        if click:
            if hasBALLZ:
                for i in range(1):
                    bouncyBALLZ.append([[mx, my], random.uniform(-2, 2), random.uniform(-3, -4.5), 5, 0])
                    num_ofBALLZ -= 3

        if num_ofBALLZ < 1:
            hasBALLZ = False
        if num_ofBALLZ > 150:
            hasBALLZ = True
        if num_ofBALLZ < 200:
            if hasBALLZ:
                num_ofBALLZ += 1
            else:
                num_ofBALLZ += 2
        for ball in bouncyBALLZ:
            pygame.draw.circle(screen2, (37, 128, 174), (ball[0][0], ball[0][1]), ball[3])
            ball[0][0] += ball[1]
            ball[0][1] += ball[2]
            ball[2] += 0.2
            ball[4] += 1
            if ball[4] > random.randint(250, 1000):
                bouncyBALLZ.remove(ball)
            if ball[0][1] > screen_height:
                ball[2] /= random.uniform(-2.5, -1.5)
                ball[0][1] = (screen_height - ball[3])

        if hasBALLZ:
            pygame.draw.rect(screen2, (37, 128, 174), pygame.Rect(4, 300 + (200 - num_ofBALLZ), 50, num_ofBALLZ), 0)
        else:
            pygame.draw.rect(screen2, (41, 128, num_ofBALLZ), pygame.Rect(4, 300 + (200 - num_ofBALLZ), 50,
                                                                          num_ofBALLZ), 0)
        pygame.draw.rect(screen2, (17, 58, 84), pygame.Rect(0, 300, 54, 200), 5)

        screen2.blit(font12.render('BALLZ', True, (37, 128, 174)), (7, 286))

    # ------------------------------ Pulsing light

    if pulsingLight_toggle:
        pygame.draw.circle(screen3, (100, 175, 200), (200, 200), 50, 0)

        y = math.sin(x)
        x += pulse_speed
        pygame.draw.circle(screen2, (75, 75, 25), (400, 200), circle_width * 2 + (y * 2 * pulse_amount), 0)
        pygame.draw.circle(screen2, (150, 150, 50), (400, 200), circle_width * 1.25 + (y * 1.25 * pulse_amount), 0)
        pygame.draw.circle(screen2, (200, 200, 75), (400, 200), circle_width/1.5 + (y/1.5 * pulse_amount), 0)
        pygame.draw.circle(screen2, (255, 255, 100), (400, 200), circle_width/3 + (y/3 * pulse_amount), 0)

    # ------------------------------ Fire particles

    if fire_toggle:
        for i in range(3):
            particles.append([[650 + random.randint(-40, 20), 250],
                              [random.randint(200, 255), random.randint(150, 200),
                               random.randint(50, 100)], 5, random.uniform(0.5, 1.5), random.uniform(-0.25, 0.25)])
        for particle in particles:
            pygame.draw.circle(screen2, particle[1], particle[0], particle[2], 0)
            particle[0][1] -= particle[3]
            particle[0][0] += particle[4]
            if particle[1][0] < 250:
                particle[1][0] += 0.5
            if particle[1][1] > 50:
                particle[1][1] -= 0.5
            if particle[1][2] > 50:
                particle[1][2] -= 0.5
            if particle[0][1] < -50:
                particles.remove(particle)

    # ------------------------------ Explosion particles

    # ------------------------------ Blit Screen and also shaking stuff

    if shaking:
        screen.blit(screen2, (random.randint(-shake_amount, shake_amount) + screenX,
                              random.randint(-shake_amount, shake_amount) + screenY))
        screen.blit(screen3, (random.randint(-shake_amount, shake_amount) + screenX,
                              random.randint(-shake_amount, shake_amount) + screenY))
    else:
        screen.blit(screen2, (screenX, screenY))
        screen.blit(screen3, (screenX, screenY))

    # ------------------------------ Update Screen

    pygame.display.update()
    clock.tick(fps)
