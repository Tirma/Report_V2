import numpy as np
import scipy.special

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# The x-values we want
x = np.linspace(-15, 15, 400)

fig, axs = plt.subplots(2, 3)

# The normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

axs[0][0].plot(x, norm_I, c='b')

xx, yy = np.meshgrid(x, x, sparse=True)
norm_I = 4 * (scipy.special.j1(np.sqrt(xx**2+yy**2)) /
              (np.sqrt(xx**2+yy**2)))**2

axs[1][0].imshow(norm_I, vmin=0, vmax=0.2)

norm_I = 4 * (scipy.special.j1(x-3.82/2) / (x-3.82/2))**2
axs[0][1].plot(x, norm_I, c='b')
norm_I = 4 * (scipy.special.j1(x+3.82/2) / (x+3.82/2))**2
axs[0][1].plot(x, norm_I, c='b')

xx, yy = np.meshgrid(x, x, sparse=True)
norm_I = 4 * (scipy.special.j1(np.sqrt(yy**2+(xx-3.82/2)**2)) /
              (np.sqrt(yy**2+(xx-3.82/2)**2)))**2 + 4 * (scipy.special.j1(np.sqrt(yy**2+(xx+3.82/2)**2)) / (np.sqrt(yy**2+(xx+3.82/2)**2)))**2

axs[1][1].imshow(norm_I, vmin=0, vmax=0.1)


norm_I = 4 * (scipy.special.j1(x-2/2) / (x-2/2))**2
axs[0][2].plot(x, norm_I, c='b')
norm_I = 4 * (scipy.special.j1(x+2/2) / (x+2/2))**2
axs[0][2].plot(x, norm_I, c='b')

xx, yy = np.meshgrid(x, x, sparse=True)
norm_I = 4 * (scipy.special.j1(np.sqrt(yy**2+(xx-2/2)**2)) /
              (np.sqrt(yy**2+(xx-2/2)**2)))**2 + 4 * (scipy.special.j1(np.sqrt(yy**2+(xx+2/2)**2)) / (np.sqrt(yy**2+(xx+2/2)**2)))**2

axs[1][2].imshow(norm_I, vmin=0, vmax=0.1)


axs[0][0].set_axis_off()
axs[0][1].set_axis_off()
axs[0][2].set_axis_off()
axs[1][0].set_axis_off()
axs[1][1].set_axis_off()
axs[1][2].set_axis_off()

plt.show()
