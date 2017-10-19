# simple implementation of spaghetti plot variants based that produce SVG files
# this is based on the UW graphics group's svgtoys wrapper for the ancient pysvg
# library
import svgtoys.elems as elems
import svgtoys.pySVGwrap as svg
import svgtoys.Charts.linegraph as linegraph

import numpy
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

def spaghetti(data, filename=False, nsamp=200,
              height = 400, ymargin=30,
              width = 640,  xmargin=40,
              **kwargs):
    # we are given the desired total size - so we need to figure out
    # how big to make the actual graph
    # the xmargin is actually used - the ymargin is a guess at how big the axis
    # label is
    graphWidth = width-xmargin
    graphHeight = height-ymargin

    # resample the signals
    resampdata = [resample(sig,nsamp) if nsamp else sig for sig in data]

    lg = linegraph.linegraph(Y=resampdata,drawPoints=False,
                             yaxisSpace=xmargin,
                             graphHeight=graphHeight, graphWidth=graphWidth,  **kwargs)
    if filename:
        elems.t1(filename,lg)
    return lg

def smallMultiples(data, filename=False,nsamp=200,
                   height=400, ymargin=30,
                   width=640, xmargin=40, spacer=10,
                   **kwargs):
    # we are given the desired total size - so we need to figure out
    # how big to make the actual graph
    # the xmargin is actually used - the ymargin is a guess at how big the axis
    # label is
    graphWidth = width-xmargin
    graphHeight = (height-ymargin-spacer*(len(data)-1))/len(data)

    # resample the signals
    resampdata = [resample(sig,nsamp) if nsamp else sig for sig in data]

    # create a linegraph for each
    lgs = [linegraph.linegraph(Y=rds,drawPoints=False,
                               graphHeight=graphHeight,
                               graphWidth=graphWidth, yaxisSpace=xmargin,
                               makeXaxis=(i==len(resampdata)-1), **kwargs)
            for i,rds in enumerate(resampdata)]

    lg = elems.elemBox(lgs,vert=True,spacer=spacer)
    if filename:
        elems.t1(filename,lg)
    return lg

def colorfield(data, filename=False, nsamp=200):
    # resample the signals
    resampdata = [resample(sig,nsamp) if nsamp else sig for sig in data]
