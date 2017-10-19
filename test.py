import datagen as DG
import simplest_matplotlib as SG
import simpleSVG as SS
import matplotlib.pyplot as PLT

from importlib import reload

d = [DG.simplestRandom(100) for i in range(5)]

if 0:
    SG.spaghetti(d)
    SG.smallMultiples(d)
    SG.colorfield(d)

SS.spaghetti(d,"d0-ss.svg")
SS.smallMultiples(d,"d0-sm.svg")