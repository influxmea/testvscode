import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 100)
y1 = np.exp(x)
y2=x*x
y3=np.sqrt(x+1)

mm = 1/25.4
fig = plt.figure(figsize=(300*mm, 50*mm))

plt.subplot(131)
plt.plot(x,y1)
plt.subplot(132)
plt.plot(x,y2)
plt.subplot(133)
plt.plot(x,y3)

plt.show()
