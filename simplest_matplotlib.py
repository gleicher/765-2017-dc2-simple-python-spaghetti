# absolute minimum implementations of the basic spaghetti plot designs
#
# written quickly by Gleicher on 10/17/2017
#
# this was meant to see how quickly I could get the basic designs in place
# I am not a matplotlib expert, so I did the simplest and first thing I could
# figure out. The plots are ugly - and the code is ugly. But it was fast to write.
#
# each of the 3 designs take a list of signals.
# there is no error checking
# everything is the defaults
#
# the one niceness: I resample the signals to length 200 - this gives smooth
# lasagna plots if the signals are shorter than 200, and does decent downsampling
# if M>200. (maybe decent - since to really get decent downsampling, I'd need to
# improve the spline fitter)

import numpy
import matplotlib.pyplot as PLT
import scipy.interpolate as INTERP


def resample(signal, numsamples):
    """
    utility routine - resamples a signal to have numsamples samples
    if signal is short (relative to numsamples) it will interpolate
    otherwise, some spline smoothing will happen

    arguably, this should be linear interpolation for the upsampling
    since we want to better preserve the shape of the data and avoid
    ringing

    :param signal: a 1D array to be resampled
    :param numsamples: number of samples to have in the result
    :return:
    """
    u = INTERP.UnivariateSpline(numpy.linspace(0, numsamples, len(signal)), signal,
                                s=0 if len(signal) < numsamples else len(signal) / 2)
    return numpy.array([u(v) for v in numpy.linspace(0, numsamples, numsamples)])


def colorfield(data):
    """
    create world's simplest colorfield (lasagna plot)
    truly ugly - but it works

    :param data: must be a list of lists/arrays
    :return:
    """
    plots = PLT.subplots(len(data), sharex=True, sharey=False)
    for i, d in enumerate(data):
        dv = resample(d, 200)
        plots[1][i].imshow([dv], aspect=5)
        plots[1][i].yaxis.set_visible(False)


def spaghetti(data):
    """
    simplest spaghetti plot - basically uses matplotlib defaults

    :param data: must be a list of lists/arrays
    :return:
    """
    # note: we need to use subplots to be consistent with the others
    plots = PLT.subplots(1, 1)
    for d in data:
        dv = resample(d, 200)
        plots[1].plot(dv)


def smallMultiples(data, doresample=True):
    """
    simplest small multiples of line graph - uses the matplotlib defaults

    :param data: must be a list of lists/arrays
    :param doresample: set to false if you don't want resampling (useful for testing
    :return:
    """
    plots = PLT.subplots(len(data), sharex=True, sharey=False)
    for i, d in enumerate(data):
        dv = resample(d, 200) if doresample else d
        plots[1][i].plot(dv)

