import pygame
from math import exp

def load_test(path, width, height):
    array = [[0 for j in range(height)] for i in range(width)]
    img = pygame.image.load(path)
    for x in range(width):
        for y in range(height):
            clr = img.get_at((x, y))
            array[x][y] = (clr[0]+clr[1]+clr[2])/3
    return array


def draw_picture(array, screen, x0, y0, scale, mode):
    max_point = 0
    min_point = 0
    if mode == 'normal':
        array = [[i*10 for i in j] for j in array]
    for x in range(len(array)):
        for y in range(len(array[0])):
            if max_point < array[x][y]:
                max_point = array[x][y]
            if min_point > array[x][y]:
                min_point = array[x][y]
    k = 255/float(max_point-min_point)
    if mode == 'normal':
        array = [[i+min_point for i in j] for j in array]
    array = [[int(i*k) for i in j] for j in array]
    for x in range(len(array)):
        for y in range(len(array[0])):
            rect = pygame.Rect(x*scale+x0, y*scale+y0, scale, scale)
            clr = max(int(array[x][y]), 0)
            pygame.draw.rect(screen, pygame.Color(clr, clr, clr, 255), rect)


def visualize(func):
    # pygame initialisation
    DISPLAY = (520, 320)
    pygame.init()
    flags = pygame.DOUBLEBUF | pygame.HWSURFACE
    screen = pygame.display.set_mode(DISPLAY, flags)
    pygame.display.set_caption("GBVS")
    background = pygame.Surface(DISPLAY)
    background.fill(pygame.Color("#000000"))

    # loading test
    path = "pgmvis/pictures/test1.bmp"
    width, height = 20, 20
    array = load_test(path, width, height)
    draw_picture(array, screen, 40, 40, 5, 'normal')
    a = func(array, 1, 1)
    draw_picture(a, screen, 290, 40, 5, 'normalized')



    # saving results
    folder = "pgmvis/pictures"
    name = "001"
    saved = False
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit
        pygame.display.update()
        if not saved:
            pygame.image.save(screen, folder+"/"+name+".bmp")
            saved = True