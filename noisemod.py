#!/usr/bin/env python
import sys
import csv
import math
import numpy
import matplotlib
from matplotlib import pyplot

"""
This module takes in a calculated set of frequencies and amplitudes to rcreate a power spectrum with soem added noise.
"""

#Set global variables
A_vel = []
nu = []
obs_error = 0
time = []

def make_noise():
    """
    Creates a time series
    """
    timeseries = obs_error * numpy.random.normal(size=len(time))
    for i in range(len(nu)):
        As = (numpy.random.normal()/numpy.sqrt(2))*A_vel[i]
        Ac = (numpy.random.normal()/numpy.sqrt(2))*A_vel[i]
        timeseries = timeseries +  As * numpy.sin(nu[i] * 2 * numpy.pi * time) + Ac * numpy.cos(nu[i] * 2 * numpy.pi * time)
    return timeseries

def setdata(freq, amp, t, obs):
    global A_vel
    global nu
    global time
    global obs_error
    A_vel = amp
    nu = freq
    time = t
    obs_error = obs

def plot():
    vel = make_noise()
    fig1 = pyplot.subplot(211)
    pyplot.plot(time,vel)
    fig1.set_title("Signal")
    fig1.set_xlabel("Time (s)")
    fig1.set_ylabel("Amplitude")
    fig2 = pyplot.subplot(212)
    ftvel = numpy.abs(numpy.fft.fft(vel))
    pyplot.plot(ftvel)
    fig2.set_title("FFT of signal")
    fig2.set_xlabel("Frequency ($\mu Hz$)")
    fig2.set_ylabel("Amplitude")
    pyplot.draw()

def add_planet(series, planetAmp, planetPeriod):
    """
    Inputs: The timeseries you with to add the planet oscilation to, the amplitude of that planets oscilation in meters/second and the planets period in days.
    Outputs: The timeseries with the planets oscillation added to it.
    """
    series = series + planetAmp*numpy.sin((1/(planetPeriod * 86400)) * 2 * numpy.pi * time) + planetAmp*numpy.cos((1/(planetPeriod * 86400)) * 2 * numpy.pi * time)
    return series
