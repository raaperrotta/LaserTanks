import numpy as np
from math import pi

"""
Controller Inputs:
    time (seconds)
    Tank (the Tank class so it's class constants are usable here)

Controller outputs:
    drive (array of left, right tread speed in units per sec)
    spin (turret rotation speed in degrees per sec)
    shoot (logical to fire laser, ignored while recharging)
"""


def R(t, Tank):
    drive = np.array([4., 1.])
    spin = 0.
    shoot = (t%3)<0.2
    return drive, spin, shoot


def G(t, Tank):
    drive = np.array([2., -2.])
    spread = Tank.body_width + Tank.tread_width - 2*Tank.tread_overlap
    w = (drive[1] - drive[0])/spread
    spin = -w*180/pi  # counter spin
    shoot = (t%4)<0.2
    return drive, spin, shoot


def B(t, Tank):
    drive = np.array([3., 5.])
    spread = Tank.body_width + Tank.tread_width - 2*Tank.tread_overlap
    w = (drive[1] - drive[0])/spread
    spin = -w*180/pi/2  # partial counter spin
    shoot = True
    return drive, spin, shoot
