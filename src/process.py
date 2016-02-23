from pgmvis.visualizer import load_test, draw_picture
from activity_map import build_activity_map
from time import clock
import pygame

# standard of pictures
X0 = 40
X1 = 290
Y0 = 40
SCALE = 5


def process_fmap(fmap, sigma, iterations, save_as):
    start = clock()
    print "STATUS: STARTING"
    try:
        #draw_picture(fmap, save_as, X0, Y0, SCALE, 'normal')
        pass
    except SystemExit:
        pass
    print "STATUS: BUILDING ACTIVITY MAP"
    try:
        fmap = build_activity_map(fmap, sigma, iterations)
        print "STATUS: ACTIVITY MAP WAS BUILT SUCCESSFULLY"
    except:
        print "STATUS: ACTIVITY MAP WAS FAILED"
    try:
        draw_picture(fmap, save_as, X1, Y0, SCALE, 'normalized', to_save=True)
    except SystemExit:
        pass
    print "STATUS: FINISHED"
    print "TOTAL TIME:", clock()-start
    print "============================================="


def full_work(path, save_as, w, h, sigma, iterations, mode='all'):
    fmap = load_test(path, w, h, mode)
    process_fmap(fmap, sigma, iterations, save_as)


def main():
    for sigma in [2, 3, 4]:
        for iterations in [0, 1, 2]:
            for mode in ["all", "r", "g", "b"]:
                full_work("pgmvis/pictures/test3.bmp", "pgmvis/pictures/"+str(sigma)+"-"+str(iterations)+"-"+mode+".bmp", 40, 40, sigma, iterations, mode)


main()
