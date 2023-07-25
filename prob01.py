import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 100)
y = np.exp(x)

mm = 1/25.4
fig = plt.figure(figsize=(100*mm, 50*mm))

plt.plot(x, y)
plt.savefig('test01.pdf',format='pdf')

y=x*x
fig = plt.figure(figsize=(100*mm, 50*mm))
plt.plot(x,y)
plt.savefig('test02.pdf',format='pdf')

y=np.sqrt(x+1)
fig = plt.figure(figsize=(100*mm, 50*mm))
plt.plot(x,y)
plt.savefig('test03.pdf',format='pdf')

