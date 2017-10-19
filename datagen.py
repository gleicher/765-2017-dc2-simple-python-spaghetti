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
import random
import numpy.random

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

def simpleRandom(m,n):
    return [simplestRandom(n) for i in range(m)]

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

# another simple data generator - maybe a little more interesting
# this creates a "year" (12 months * 30 days per month)
# the months alternate between good and bad
# one month is really good
# there are a few days (peakDays) where
def randYear(oddEven=0, bestMonth=-1, peakDays=[], peakValue=90, bestMonthVal=70):
    # this code is ugly since we need to have multiple knots per month
    # make an interpolation point at the beginning and end of each month
    ipts = []
    for i in range(12):
        ipts.append(float(i)+.25)
        ipts.append(float(i)+.5)
        ipts.append(float(i)+.75)
    ipts[0] = 0
    ipts[-1] = 12

    # for each month, alternate between 20-40 and 40-60
    vals = []
    for i in range(12):
        v = random.random()*20 + 20 + ((i+oddEven)%2) * 20
        vals.append(v)
        vals.append(v)
        vals.append(v)
    # one month, it goes up a lot
    if bestMonth < 0:
        bestMonth = int(random.random()*12)
    vals[bestMonth*3] = bestMonthVal
    vals[bestMonth*3+1] = bestMonthVal
    vals[bestMonth*3+2] = bestMonthVal
    ms = INTERP.UnivariateSpline(ipts,vals,s=0)

    # add a higher frequency random pattern
    wkeys = [random.random() * 10 - 5 * (i%2) for i in range(12*4)]
    ws = INTERP.UnivariateSpline(numpy.linspace(0,12,len(wkeys)),wkeys,s=0)

    days = [ms(u)+ws(u) for u in numpy.linspace(0,12,360)]

    # and a few peak days
    peakDays = sorted(peakDays)
    # make sure the peak days are at least 6 days apart so we can fit keys
    for i in range(len(peakDays)-1):
        if peakDays[i]+8 > peakDays[i+1]:
            peakDays[i+1] = peakDays[i]+6

    for p in peakDays:
        delta = peakValue-days[p]
        days[p-1] += delta/2
        days[p+1] += delta/2
        days[p] += delta

    return days

def weirdSet(nsigs):
    badDays = [50,100,160,170,200,300,320]
    data = [ randYear(i,peakDays=numpy.random.choice(badDays,3,replace=False)) for i in range(nsigs) ]
    return data
