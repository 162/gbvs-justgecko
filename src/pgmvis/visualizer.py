import pygame
from math import exp
from time import clock, sleep

def load_test(path, width, height, mode):
    array = [[0 for j in range(height)] for i in range(width)]
    img = pygame.image.load(path)
    for x in range(width):
        for y in range(height):
            clr = img.get_at((x, y))
            if mode == "a":
                array[x][y] = (clr[0]+clr[1]+clr[2])/3
            if mode == "r":
                array[x][y] = clr[0]
            if mode == "g":
                array[x][y] = clr[1]
            if mode == "b":
                array[x][y] = clr[2]
    return array


def draw_picture(array, save_as, x0, y0, scale, mode, to_save=False):
    DISPLAY = (len(array)*scale, len(array[0])*scale)
    pygame.init()
    flags = pygame.DOUBLEBUF | pygame.HWSURFACE
    # screen = pygame.display.set_mode(DISPLAY)
    screen = pygame.display.set_mode(DISPLAY, flags)
    pygame.display.set_caption("GBVS")
    background = pygame.Surface(DISPLAY)
    background.fill(pygame.Color("#000000"))
    #DRAWING
    max_point = 0
    min_point = 0
    if mode == 'normalized':
        array = [[i*10 for i in j] for j in array]
    for x in range(len(array)):
        for y in range(len(array[0])):
            if max_point < array[x][y]:
                max_point = array[x][y]
            if min_point > array[x][y]:
                min_point = array[x][y]
    k = 255/float(max_point-min_point)
    if mode == 'normalized':
        array = [[i-min_point for i in j] for j in array]
    array = [[int(i*k) for i in j] for j in array]
    #print array
    for x in range(len(array)):
        for y in range(len(array[0])):
            rect = pygame.Rect(x*scale+x0, y*scale+y0, scale, scale)
            clr = max(int(array[x][y]), 0)
            pygame.draw.rect(screen, pygame.Color(clr, clr, clr, 255), rect)
    pygame.display.update()
    if to_save:
        pygame.image.save(screen, save_as)
    raise SystemExit


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
    #print array
    start = clock()
    a = func(array, 1, 1)
    print clock()-start
    #print a
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
        path = "pgmvis/pictures/test2.bmp"
        width, height = 40, 40
        array = load_test(path, width, height)
        draw_picture(array, screen, 40, 40, 5, 'normal')
        #print array
        start = clock()
        a = func(array, 3, 1)
        print clock()-start
        #print a
        draw_picture(a, screen, 290, 40, 5, 'normalized')
        pygame.display.update()
        pygame.image.save(screen, folder+"/002.bmp")
        path = "pgmvis/pictures/test2.bmp"
        width, height = 40, 40
        array = load_test(path, width, height)
        draw_picture(array, screen, 40, 40, 5, 'normal')
        #print array
        start = clock()
        a = func(array, 4, 1)
        print clock()-start
        #print a
        draw_picture(a, screen, 290, 40, 5, 'normalized')
        pygame.display.update()

        break


def draw_merged_picture(features, save_as, x0, y0, scale, mode, to_save=False):
    DISPLAY = (len(features[0])*scale, len(features[0][0])*scale)
    pygame.init()
    flags = pygame.DOUBLEBUF | pygame.HWSURFACE
    # screen = pygame.display.set_mode(DISPLAY)
    screen = pygame.display.set_mode(DISPLAY, flags)
    pygame.display.set_caption("GBVS")
    background = pygame.Surface(DISPLAY)
    background.fill(pygame.Color("#000000"))
    #DRAWING
    max_point = 0
    min_point = 1000
    if mode == 'normalized':
        features = [[[i*10 for i in j] for j in k] for k in features]
    for q in range(len(features)):
        for x in range(len(features[q])):
            for y in range(len(features[q][0])):
                if max_point < features[q][x][y]:
                    max_point = features[q][x][y]
                if min_point > features[q][x][y]:
                    min_point = features[q][x][y]
        k = 255/float(max_point-min_point)
        features[q] = [[min(255, i*k) for i in j] for j in features[q]]
        max_point = 0
        min_point = 1000
    print "STATUS: UPDATED"
    for x in range(len(features[0])):
        for y in range(len(features[0][0])):
            rect = pygame.Rect(x*scale+x0, y*scale+y0, scale, scale)
            clr = max(int((sum(features[i][x][y] for i in range(len(features)))/len(features))), 0)
            #print features[0][x][y], features[1][x][y], features[2][x][y], features[3][x][y], clr
            pygame.draw.rect(screen, pygame.Color(clr, clr, clr, 255), rect)
            #sleep(0.01)
            pygame.display.update()
    if to_save:
        pygame.image.save(screen, save_as)
    print "saved to ", save_as
    sleep(10)
    raise SystemExit