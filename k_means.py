from sys import argv
from getopt import getopt
from sklearn.cluster import k_means as means
from osgeo import gdal
import numpy


def get_arguments():
    if len(argv) < 2:
        return
    arguments = argv[1:]
    opts, args = getopt(arguments, 'n:i:fi:fo:', ['n=', 'iter=', 'file-input=', 'file-output='])
    for o, a in opts:
        if o == '-n':
            n = int(a)
        elif o == '-i':
            iter = int(a)
        elif o == '-fi':
            input_file = a
        elif o == '-fo':
            output_file = a
    return n, iter, input_file, output_file


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
    numpy.save(filename, array)
    print ("File saved successfully. \n")


if __name__ == '__main__':
    if get_arguments() is not None:
        print ('ok.')
        #n, iter, input_file, output_file = get_arguments()

    else:
        n = int(raw_input('Type number of cluster to create:'))
        iter = int(raw_input('Type maximum number of iterations:'))
        input_file = raw_input('Input filename with extension:')
        output_file = raw_input('Type output filename:')

        array = load_bsq_to_array(input_file)
        result = k_means(n, iter, array)
        save_result(result, output_file)

