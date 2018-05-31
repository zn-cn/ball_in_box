# -*- coding: utf-8 -*-
import math
import sys
from ball_in_box import config

__all__ = ['ball_in_box']




def ball_in_box(num_of_circle, blockers):
    """
        Main body of algorithm: Greedy Algorithm
    """
    xrange = config.XRANGE
    yrange = config.YRANGE
    percision = config.PERCISION
    circles = []
    dots = prod_dots(xrange, yrange, percision)
    for i in range(num_of_circle):
        temp_r = 0
        circle = [0, 0, 0]
        for dot in dots:
            r = get_max_r(dot, xrange, yrange, blockers, circles)
            if r > temp_r:
                temp_r = r
                circle[0] = dot[0]
                circle[1] = dot[1]
                circle[2] = temp_r

        dots.remove((circle[0], circle[1]))
        circles.append((circle[0], circle[1], circle[2]))

    return circles
