# Problem Link: https://www.codingninjas.com/studio/problems/check-whether-k-th-bit-is-set-or-not_5026446

# Solution:
from typing import *
def isKthBitSet(n: int, k: int) -> bool:
    shifter = 1 << (k-1)
    out = (n & shifter) >> (k - 1)
    return out == 1


# Notes:
# * This is te best solution