import datagen as DG
import simplest_matplotlib as SG
import matplotlib.pyplot as PLT

d = [DG.simplestRandom(100) for i in range(5)]

SG.spaghetti(d)
SG.smallMultiples(d)
SG.colorfield(d)