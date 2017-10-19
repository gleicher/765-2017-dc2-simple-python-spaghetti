import datagen as DG
import simplest_matplotlib as SG
#import simpleSVG as SS
import matplotlib.pyplot as PLT

from importlib import reload


if 0:
    d = [DG.simplestRandom(100) for i in range(5)]
    SG.spaghetti(d)
    SG.smallMultiples(d)
    SG.colorfield(d)

w5 = DG.weirdSet(5)
w10 = DG.weirdSet(10)
SG.colorfield(w10)
SG.colorfield(w10,0)
