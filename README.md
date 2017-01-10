# k-means-bsq
Utility to cluster *.bsq files using k-means algorithm.

# Description
Script to cluster Landsat 7 and 8 imagery in ENVI file extension(*.bsq - Band Sequential Data, *.hdr - ENVI header file) using k-means algorithm.


# Requirements:
 - Python >=2.7
 - Numpy >= 1.8
 - GDAL >= 1.9
 - scikit-learn >= 0.18
 
# Usage:
Parameters:
 - -n or n= number of cluster to create
 - -i or iter= maximum number of iterations
 - -fi or file-input= name of input file
 - -fo or file-output= name of output file
 
Examples:

Below two equivalent examples:

```shell
python test.py -n 8 -i 300 -fi dem-400.bsq -fo output.npy
python test.py n=8 iter=300 file-input=dem-400.bsq file-output=output.npy```

You can also run simply python test.py and program will ask for parameters.

