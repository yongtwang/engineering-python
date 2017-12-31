import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(0, 2*np.pi, 0.1)
fig = plt.figure(figsize=(5, 4), dpi=80)
lines = plt.plot(x, np.sin(x), x, np.cos(x))  # Returns a list of two lines

frames=np.arange(20)

def animate(i):
    lines[0].set_ydata(np.sin(x + i/10.0))  # update the sine curve
    lines[1].set_ydata(np.cos(x + i/10.0))  # update the cosine curve
    return lines

ani = animation.FuncAnimation(fig=fig, func=animate, frames=frames, interval=100, repeat=False)
plt.show()