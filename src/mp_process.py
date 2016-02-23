import multiprocessing.dummy as multiprocessing
from time import clock
from process import *

def process(n, sigma, iterations, mode):
    filename = "pgmvis/pictures/" + str(n) + "-" + str(int(2*sigma)) + "-" + str(iterations) + "-" + mode + ".bmp"
    print "PROCESSING:", filename
    full_work("pgmvis/pictures/test"+str(n)+".bmp", filename, 20, 20, sigma, iterations, mode)

p = multiprocessing.Pool()
p.map(lambda mode: process(1, 2, 0, mode), ['r', 'g', 'b'])
p.close()
p.join()
