# Sparse Distributed Memory for Python

## What is this?

This is a fast implementation of Pentti Kanerva's [Sparse Distributed Memory (SDM)](https://en.wikipedia.org/wiki/Sparse_distributed_memory). `sdmlib` is written in Python using [`numpy`](https://numpy.org).

## Installation

The package is available through PyPi:
```sh
pip install sdmlib
```

## Using `sdmlib`

`sdmlib` is designed to operate on `numpy` arrays.

### The `Memory` class

This class provides the main functionality of SDM.

|Parameter|Description|
|:-:|:-:|
|`N`|Length of addresses in bits|
|`M`|Number of hard addresses|
|`U`|Length of data in bits|
|`d`|Hamming radius of addresses considered "near" for reading and writing. If `None`, then it is computed using T|
|`T`|(Default: `None`) Number of data points to be written. Ignored if `d` is provided. If `T` is `None` then `d` must be provided. `d` and `T` cannot both be `None`|
|`seed`|Seed the random number generator (for reproducability)|

### Example Usage

```python
import numpy as np
from sdmlib import Memory

N = 256
M = 1000
U = 256
T = 100

addresses =  np.random.randint(low=0, high=2, size=(T, N), dtype=np.uint8)
data      =  np.random.randint(low=0, high=2, size=(T, U), dtype=np.uint8)

mem = Memory(N=N, M=M, U=U, d=None, T=T)

for t in range(T):
    mem.write(addresses[t], data[t])

error = 0
for t in range(T):
    error += np.mean(data[t] != mem.read(addresses[t]))/T
print(f'Reconstruction error: {100*error:.2f}%')
```

```
Reconstruction error: 0.51%
```

#### The `write` method
Write a binary string to memory.

|Parameter|Description|
|:-:|:-:|
|`x`|Address. Binary numpy array of shape `(N,)`|
|`w`|Data. Binary numpy array of shape `(U,)`|

#### The `read` method
Read a binary string from memory.

|Parameter|Description|
|:-:|:-:|
|`x`|Address. Binary numpy array of shape `(N,)`|

|Returns|Description|
|:-:|:-:|
|`z`|Data. Binary numpy array of shape `(U,)`|
