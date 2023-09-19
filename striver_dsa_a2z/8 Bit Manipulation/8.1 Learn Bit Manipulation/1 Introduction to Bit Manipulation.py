# Problem Link: https://www.codingninjas.com/studio/problems/bit-manipulation_8142533

# Solution:
from typing import *

def bitManipulation(num : int, i : int) -> List[int]:
    shifter = 1 << (i-1)

    out1 = (num & shifter) >> (i-1)
    out2 = num | shifter
    out3 = num & ~shifter
    
    return [out1, out2, out3]

# Notes:
# * This is te best solution