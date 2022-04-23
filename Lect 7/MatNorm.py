import numpy as np
from scipy.linalg import hilbert

H = hilbert(5)
print(np.linalg.cond(H))