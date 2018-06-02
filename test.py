from scipy.optimize import fsolve
from itertools import combinations

three_cond = [(1, 2, 3), (1, 2, 1)]
res = [cond for cond in three_cond if cond[2] != 1]
print(res)