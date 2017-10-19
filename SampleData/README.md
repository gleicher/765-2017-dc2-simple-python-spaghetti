# Sample Data

This directory contains some sample data for the spaghetti plot programs.
It generates some simple random data using the routines in "datagen".

It's mainly here so if you need some sample data but don't want to run
the python scripts, you can just access it from the repo.

### Simple Random

These are various sized data sets that are purely random.
They are designed to be smooth so they look nicer when plotted.

There are 3 or 10 lines, with 50 or 200 samples per line.

### The "Weird Data"

This simulates "years" (except that they are 12 months each with 30 days).
So each line has 360 samples.

Months alternate between high and low, with one "very high" month thrown in
randomly. And a few spurious days where things spike - with these spikes 
designed to co-occur. And extra randomness thrown in. 

It's nothing special, but it gives you *something* to look at.
In a spaghetti plot, it's hard to see the spike coocurrance (or much of anything).
In other views, you can pick out the different phenomena.

There are data sets with 5 and 10 lines (of 360 samples).