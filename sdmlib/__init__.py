import scipy.stats as st
import numpy as np
from time import time

class Memory:
    def __init__(self, N, M, U, d, T=None, seed=None):
        """
        |Parameter|Description|
        |:-:|:-:|
        |`N`|Length of addresses in bits|
        |`M`|Number of hard addresses|
        |`U`|Length of data in bits|
        |`d`|Hamming radius of addresses considered "near" for reading and writing. If `None`, then it is computed using T|
        |`T`|(Default: `None`) Number of data points to be written. Ignored if `d` is provided. If `T` is `None` then `d` must be provided. `d` and `T` cannot both be `None`|
        |`seed`|Seed the random number generator (for reproducability)|
        """
        if d is None:
            if T is None:
                raise ValueError(f'd and T cannot both be None.')
            else:
                # Optimality conditions found by Kanerva for uniformly
                # distributed addresses where z is a function that takes a
                # probability and returns a z score.
                d = N/2 + st.norm.ppf((2*M*T)**(-1/3.)) * (N/4)**(1/2)

        self.N = N
        self.M = M
        self.d = d

        np.random.seed(seed)

        self.A = np.random.randint(low=0, high=2, size=(M, N), dtype=np.uint8)
        self.C = np.zeros((M, U), dtype=np.int8)

    def write(self, x, w):
        """
        Write a binary string to memory.
        |Parameter|Description|
        |:-:|:-:|
        |`x`|Address. Binary numpy array of shape `(N,)`|
        |`w`|Data. Binary numpy array of shape `(U,)`|
        """
        d = np.logical_xor(x, self.A).sum(axis=1)
        y = np.where(d < self.d)
        self.C[y] += -1 + 2*w

    def read(self, x):
        """
        |Parameter|Description|
        |:-:|:-:|
        |`x`|Address. Binary numpy array of shape `(N,)`|

        |Returns|Description|
        |:-:|:-:|
        |`z`|Data. Binary numpy array of shape `(U,)`|
        """
        d = np.logical_xor(x, self.A).sum(axis=1)
        y = np.where(d < self.d)
        s = self.C[y].sum(axis=0)
        z = (s > 0).astype(np.uint8)
        return z
