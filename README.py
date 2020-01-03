# Python code found in README.md

import numpy as np
from sdmlib import Memory

N = 256   # length of addresses
M = 1000  # number of hard addresses
U = 256   # length of data
T = 100   # number of data patterns to store

addresses =  np.random.randint(low=0, high=2, size=(T, N), dtype=np.uint8)
data      =  np.random.randint(low=0, high=2, size=(T, U), dtype=np.uint8)

mem = Memory(N=N, M=M, U=U, d=None, T=T)

for t in range(T):
    mem.write(addresses[t], data[t])

error = 0
for t in range(T):
    error += np.mean(data[t] != mem.read(addresses[t]))/T
print(f'Reconstruction error: {100*error:.2f}%')
