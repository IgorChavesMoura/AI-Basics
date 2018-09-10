import numpy as np
from numpy import linalg as LA

x1 = np.array([ 0.5377,  0.3188,  3.5784, 0.7254])
x2 = np.array([-2.2588, -0.4336, -1.3499, 0.7147])
x3 = np.array([-2.2588, -0.4336, -1.3499, 0.7147])
x4 = np.array([ 0.8622,  0.3426,  3.0349,-0.2050])

x = [x1,x2,x3,x4]


I1 = [LA.norm(xi, ord=1) for xi in x]
I2 = [LA.norm(xi, ord=2) for xi in x]

print(I1)

print(I2)


delta = [xi - xj for xj in x for xi in x]

print(delta)

E = [xi + xj for xj in x for xi in x]

K = [xi * xj for xj in x for xi in x]

D = [LA.norm(xi - xj, ord=2) for xj in x for xi in x]

# =====================================================

X1 = []
X2 = []

e = 0.01

for xi in x:

	i = [None,xi]
	k = 1

	i.append(i[k] + (1/k)*i[k])

	k = k + 1

	while LA.norm(i[k] - i[k-1],ord=2) > e or K < 10000:


		i.append(i[k] + (1/k)*i[k])

		k = k + 1

	X1.append(i)

print(X1)



for xi in x:

	i = [None,xi]
	k = 1

	i.append(i[k] - (1/k)*i[k])

	k = k + 1

	while LA.norm(i[k] - i[k-1],ord=2) > e or K < 10000:


		i.append(i[k] - (1/k)*i[k])

		k = k + 1

	X2.append(i)

print(X2)

