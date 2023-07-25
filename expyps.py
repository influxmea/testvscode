import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 100)
y = np.exp(x)

mpl.rcParams['text.usetex'] = True

mm = 1/25.4
fig = plt.figure(figsize=(174*mm, 44*mm))

plt.plot(x, y, label=r'$\alpha > \beta$')
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('test01.pdf',format='pdf')
