from pgmvis.visualizer import load_test, draw_picture, draw_merged_picture
from activity_map import build_activity_map
from time import clock
import pygame

# standard of pictures
X0 = 0
X1 = 290
Y0 = 0
SCALE = 10


def process_fmap(fmap, sigma, iterations, save_as):
    start = clock()
    print "STATUS: STARTING"
    print "STATUS: BUILDING ACTIVITY MAP"
    try:
        fmap = build_activity_map(fmap, sigma, iterations)
        print "STATUS: ACTIVITY MAP WAS BUILT SUCCESSFULLY"
    except:
        print "STATUS: ACTIVITY MAP WAS FAILED"
    try:
        draw_picture(fmap, save_as, X0, Y0, SCALE, 'normalized', to_save=True)
    except SystemExit:
        pass
    print "STATUS: FINISHED"
    print "TOTAL TIME:", clock()-start
    print "============================================="


def full_work(path, save_as, w, h, sigma, iterations, mode='a'):
    fmap = load_test(path, w, h, mode)
    process_fmap(fmap, sigma, iterations, save_as)


def full_for_all(path, save_as, w, h, sigma, iterations, mode):
    features = [load_test(path, w, h, m) for m in mode]
    features = [build_activity_map(i, sigma, iterations) for i in features]
    draw_merged_picture(features, save_as, 0, 0, 10, "normalized", True)


def main():
    start = clock()
    for n in [5]:
        for sigma in [2, 2.5, 3, 3.5, 4]:
            for iterations in [0, 1, 2]:
                for mode in ["all", "r", "g", "b"]:
                    filename = "pgmvis/pictures/" + str(n) + "-" + str(int(2*sigma)) + "-" + str(iterations) + "-" + \
                               mode + ".bmp"
                    print "PROCESSING:", filename
                    try:
                        full_work("pgmvis/pictures/test"+str(n)+".bmp", filename, 40, 40, sigma, iterations, mode)
                    except:
                        pass
    t = clock()-start
    print 'total time for 3*5*3*4 =',  t
    print 'per one =', t/180


#main()
for j in [[5, 1], [5, 2], [6, 0], [6, 1], [6, 2]]:
    for i in ['6', '7', '8', '9', '10', '11', '12', '13']:
        start = clock()
        try:
            full_for_all("pgmvis/pictures/tests/test"+i+".bmp", 'pgmvis/pictures/results/rgb/' + str(j[0]) + '-' +
                         str(j[1])+'/' + i + '.bmp', 64, 48, j[0], j[1], 'rgb')
        except SystemExit:
            print clock()-start