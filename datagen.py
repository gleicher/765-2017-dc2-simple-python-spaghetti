# generate random signals - as well as load and save signals
#
# useful for testing spaghetti plot designs
# most of the random signal generators are simple
#
# note that our "data format" is a list of signals (NOT a numpy array)
# where a signal is either a list or a numpy array
#
# the file format writes the data into COLUMNS

import numpy
import scipy.interpolate as INTERP
import csv
import pandas

def simplestRandom(n):
    """
    make a random signal - so we have something to look at
    :param n:
    :return:
    """
    # do something "perlin noise like" - with various frequency scales
    level1 = numpy.random.randint(0,4,size=4)
    level2 = numpy.random.randn(10)
    level3 = numpy.random.randn(50) * .5
    # make splines for each
    u1 = INTERP.UnivariateSpline(numpy.linspace(0,1,4) ,level1,s=0)
    u2 = INTERP.UnivariateSpline(numpy.linspace(0,1,10),level2,s=0)
    u3 = INTERP.UnivariateSpline(numpy.linspace(0,1,50),level3,s=0)
    # build the signal on the range 0..1 - then use linspace to sample it
    samples = numpy.linspace(0,1,n)
    return numpy.array([u1(u)+u2(u)+u3(u) for u in samples])

def writeData(fname,data):
    """
    write out our data form (list of arrays) to our file format (lines in columns)
    :param fname: file name
    :param data:
    :return:
    """
    with open(fname,"w",newline="") as fo:
        wr = csv.writer(fo)
        wr.writerow(["x"]+["Series {}".format(i+1) for i in range(len(data))])
        # just in case things are of different lengths
        n = max([len(d) for d in data])
        for i in range(n):
            lst = [i]
            for d in data:
                try:
                    val = d[i]
                except IndexError:
                    val = 0
                lst.append(val)
            wr.writerow(lst)

def readData(fname):
    """
    read in a csv file that is of the right form - rotate it (so each column is a signal)
    :param fname:
    :return:
    """
    pd = pandas.read_csv(fname)
    return [numpy.array(pd[colname]) for colname in pd.columns[1:]]


