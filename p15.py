import numpy as np

import math

n = 20

# the problem can be reduced to a combanatorial problem like so 
# find all possible ways you can write a string of length 2n using 
# D (down) and R (right) where you can only make n moves of each:
# we only need to choose the positions of one letter for example D
# then we'd know where the R letters go

print(math.comb(2*n, n)) # 137846528820
