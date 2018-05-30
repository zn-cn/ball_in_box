# -*- coding: utf-8 -*-
import math
import ball_in_box.ballinbox as bb
import ball_in_box.validate as val
# import random
from ball_in_box import config


def area_sum(circles):
    """
        Calculating the area
    """
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area


# def prod_blockers(num):
#     """
#         Generating blockers
#     """
#     blockers = []
#     for i in range(num):
#         x = (XRANGE[1] - XRANGE[0]) * random.random() + XRANGE[0]
#         y = (YRANGE[1] - YRANGE[0]) * random.random() + YRANGE[0]
#         blockers.append((x, y))
#     return blockers


def print_condition(num_of_blockers, xrange, yrange, blockers):
    """
        Printing the condition
    """
    print("条件：")
    print("NUM_OF_BLOCKERS: ", num_of_blockers)
    print("XRANGE: ", xrange)
    print("YRANGE: ", yrange)
    print("blockers: ", blockers, "\n")


def print_circles(circles):
    """
        Printing the circles
    """
    for item in circles:
        print("(x, y) -> (%10.6f, %10.6f), r -> %10.6f" % (item[0], item[1],
                                                           item[2]))
    print("\n")


if __name__ == '__main__':
    # Randomly generating the blockers
    # blockers = prod_blockers(NUM_OF_BLOCKERS)
    blockers = [(0.5, 0.5), (0.5, -0.3)]
    num_of_blockers = config.NUM_OF_BLOCKERS
    xrange = config.XRANGE
    yrange = config.YRANGE
    num_of_circle = config.NUM_OF_CIRCLE
    print_condition(num_of_blockers, xrange, yrange, blockers)
    circles = bb.ball_in_box(num_of_circle, blockers)
    print("circles: ")
    print_circles(circles)

    # To determine whether or not to meet the conditions
    if num_of_circle == len(circles) and val.validate(circles, blockers):
        area = area_sum(circles)
        print("Total area: {}".format(area))
    else:
        print("Error: no good circles.")
