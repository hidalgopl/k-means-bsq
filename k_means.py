# import scipy
# import os
from sys import argv
from getopt import getopt
from sklearn.cluster import KMeans
from osgeo import gdal
import spectral
import numpy


def get_arguments():
    if len(argv) < 2:
        return
    arguments = argv[1:]
    opts, args = getopt(arguments, 'n:i:', ['n=', 'iter='])
    for o, a in opts:
        if o == '-n':
            n = int(a)
        if o == '-i':
            iter = int(a)
    return n, iter


def load_bsq_to_array(filename):
    driver = gdal.GetDriverByName('ENVI')
    img = gdal.Open(filename)
    band = img.GetRasterBand(1)
    data = band.ReadAsArray()
    print ('Data successfully loaded to array. \n')
    return data


def k_means(n, iter, array, verbose=0):
    result = KMeans(n_clusters=n, max_iter=iter, verbose=verbose).fit(array)
    return result


def save_result(array, filename):
    numpy.save(filename, array)
    print ("File saved successfully. \n")


if __name__ == '__main__':
    if get_arguments() is not None:
        print ('bla')

    else:
        n = int(raw_input('Type number of cluster to create:'))
        iter = int(raw_input('Type maximum number of iterations:'))
        input_file = raw_input('Input filename with extension:')
        output_file = raw_input('Type output filename:')
        array = load_bsq_to_array(input_file)
        result = k_means(n, iter, array)
        save_result(result, output_file)
