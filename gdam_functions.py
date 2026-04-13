"""Functions used in the Introduction to Quantitative Geology course"""

import math
import numpy as np


def gaussian(x, mean, std):
    return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))