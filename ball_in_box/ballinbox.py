# -*- coding: utf-8 -*-
from itertools import combinations
from scipy.optimize import fsolve
from ball_in_box import config
import copy


def isvalid(circle, other_circle):
    """
        Whether two circles do not intersect?
    """
    if other_circle[0] == config.BORDER:
        return circle[0] + circle[2] <= 1.0
    elif other_circle[0] == -config.BORDER:
        return circle[0] - circle[2] >= -1.0
    elif other_circle[1] == config.BORDER:
        return circle[1] + circle[2] <= 1.0
    elif other_circle[1] == -config.BORDER:
        return circle[1] - circle[2] >= -1.0
    else:
        return (circle[2] + other_circle[2])**2 <= (
            circle[0] - other_circle[0])**2 + (circle[1] - other_circle[1])**2


def validate(circle, circles):
    """
        Is the verification condition established?
    """
    for test_circle in circles:
        if not isvalid(circle, test_circle):
            return False
    return True


# 解方程
def solve_equations(three_conds, solution0):
    """
        @param three_conds: List[set]
        @param solution0: List or set
        @res solve: List
        Solving equations
    """

    def fi(solution0, cond):
        """
            Homogeneous equation
        """
        x, y, r = solution0
        xi, yi, ri = cond
        if xi == config.BORDER:
            return x + r + config.XRANGE[0]
        elif xi == -config.BORDER:
            return x - r + config.XRANGE[1]
        elif yi == config.BORDER:
            return y + r + config.YRANGE[0]
        elif yi == -config.BORDER:
            return y - r + config.YRANGE[1]
        else:
            return (x - xi)**2 + (y - yi)**2 - (r + ri)**2

    def f(x):
        return [fi(x, cond) for cond in three_conds]

    return fsolve(f, solution0)


def ball_in_box(m, blockers):
    """
        @param m: int
        @param blockers: List or set
        @res circles: List
        Main body of algorithm: Greedy Algorithm
    """
    circles = []
    conditions = copy.copy(config.CONDITIONS)
    for blocker in blockers:
        conditions.append((blocker[0], blocker[1], 0))

    for i in range(m):
        max_circle = [0, 0, 0]
        for three_conds in combinations(conditions, 3):
            solves = [[x, y, 0] for x in [-1, 1] for y in [-1, 1]]
            for s in solves:
                new_circle = solve_equations(three_conds, s)
                if validate(new_circle,
                            conditions) and new_circle[2] > max_circle[2]:
                    max_circle = new_circle
        conditions.append(max_circle)
        circles.append(max_circle)
    return circles
