from matplotlib.pyplot import *
from numpy import *

x = arange(0,10.5,0.5)
N = len(x)
for i in range(N):
	y = x[i]
	print(y)

print("\n")
for i in range(N):
	z = x[i]**2
	print(z)

