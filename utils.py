from sys import argv
from getopt import getopt
from sklearn.cluster import k_means as means
from osgeo import gdal
from osgeo.gdalconst import GDT_CFloat32
import math
import numpy


def get_arguments():
    if len(argv) < 2:
        return
    arguments = argv[1:]
    opts, args = getopt(arguments, 'n:t:i:o:', ['n=', 't=', 'i=', 'o='])
    options = {}
    for o, a in opts:
        if o == '-n':
            options['n'] = int(a)
        elif o == '-t':
            options['t'] = int(a)
        elif o == '-i':
            options['i'] = a
        elif o == '-o':
            options['o'] = a
    return options


def load_bsq_to_array(filename):
    driver = gdal.GetDriverByName('ENVI')
    img = gdal.Open(filename)
    band = img.GetRasterBand(1)
    data = band.ReadAsArray()
    print ('Data successfully loaded to array. \n')
    return data


def k_means(n, iter, array, verbose=False):
    result = means(X=array, n_clusters=n, max_iter=iter, verbose=verbose)
    return result


def save_result(array, filename):
    if '.' not in filename:
        filename += '.bsq'
    if filename.split('.')[1] != 'bsq':
        filename = filename.split('.')[0] + '.bsq'
    output_array = numpy.array(array[1])
    k = int(math.sqrt(output_array.shape[0]))
    output_array = output_array.reshape(k, k)
    driver = gdal.GetDriverByName('ENVI')
    outfile = driver.Create(filename, k, k, 1, GDT_CFloat32)
    outfile.GetRasterBand(1).WriteArray(output_array, 0, 0)
    print ("File saved successfully. \n")
