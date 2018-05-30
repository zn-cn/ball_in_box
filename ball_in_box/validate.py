# -*- coding: utf-8 -*-
from ball_in_box import config


def validate(circles, blockers):
    xrange = config.XRANGE
    yrange = config.YRANGE
    # Is circle in the box?
    for circle in circles:
        xmr = circle[0] - circle[2]
        xpr = circle[0] + circle[2]
        ymr = circle[1] - circle[2]
        ypr = circle[1] + circle[2]

        if not xmr <= xrange[1] and xmr >= xrange[0]  \
           or not xpr <= xrange[1] and xpr >= xrange[0] \
           or not ymr <= yrange[1] and ymr >= yrange[0]  \
           or not ypr <= yrange[1] and ypr >= yrange[0]:
            return False

    # Is circle good for blockers?
    if blockers is not None and len(blockers) > 0:
        for circle in circles:
            for block in blockers:
                x = circle[0]
                y = circle[1]
                r = circle[2]
                bx = block[0]
                by = block[1]
                # Due to the precision problem of floating-number calculation,we set a deviation range : 1e-8
                if (x - bx)**2 + (y - by)**2 < (r**2 - 1e-8):
                    return False

    # Is circle good for each other?
    for index1, value1 in enumerate(circles):
        for index2, value2 in enumerate(circles):
            if index1 != index2:
                x1 = value1[0]
                y1 = value1[1]
                r1 = value1[2]
                x2 = value2[0]
                y2 = value2[1]
                r2 = value2[2]
                # Due to the precision problem of floating-number calculation,we set a deviation range : 1e-8
                if (x1 - x2)**2 + (y1 - y2)**2 < ((r1 + r2)**2 - 1e-8):
                    return False

    # all good
    return True
