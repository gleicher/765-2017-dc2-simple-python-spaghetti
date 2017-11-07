# 765-2017-dc2-simple-python-spaghetti
Simple Python Implementation of Spaghetti Plots (and data generation) for CS765 DC2, Fall, 2017

This code was written by Mike Gleicher, in a hurry, in October 2017.

You are welcome to use it as a starting point for your assignment - but remember
to give proper attribution.

I used Python 3.6, and the code uses various libraries (scipy, pandas, matplotlib...).
These are all pretty standard.

## Simple Matplotlib Implementation

**simplest_matplotlib.py** has the simplest implementation of the basic chart types
I could think of.

It resamples the signals to make smooth charts - which also handles cases where you have
long signals. Resampling may not be what you want though (since it can remove fine details).

The x axes are wrong - they give the numbering for the resampled signals.

Overall, these are really ugly. In general, Matplotlib makes ugly stuff. 
It is possible to tweak matplotlib to be less ugly, but I haven't done it.

I also didn't include the color legend - it's easy to do (matplotlib has a function
called "colorbar" that does it for you). However, whenever I made a colorbar, it
put it in a  weird place.

These can serve as a starting point - or provide a reference implementation
to check data sets. I hope that student implementations look nicer.

## Basic Data Generator

**datagen.py** has some basic utility routines for reading and writing data files,
and for generating random data to test things out with.

There is a **SampleData** directory that has CSV files I computed with datagen.
It's easy enough for you to make them as well - but it requires you to have the right
version of python lying around.

## D3 (Javascript) version

Florian created a version in Javascript using D3. It's in a different repo:
[https://github.com/uwgraphics/pastavis](PastaVis Repo).
A version running on the web is
[https://pages.cs.wisc.edu/~heimerl/pasta/](on Florian's home page).
You can load the sample data into it.

## SVG version

I started writing a version of the basic charts using an SVG library that 
we have in our group. I never finished it. Things look just as ugly as 
matplotlib, and it requires a weird library that isn't documented. So
ignore it. I should probably remove it from the repo.
