import numpy as np
from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

# Use seaborn to change the default graphics to something nicer
import seaborn as sns
# And set a nice color palette
sns.set_color_codes('deep')

# Create the plot object
fig, ax = plt.subplots(figsize=(5, 4))
x1 = np.linspace(0, 100)

# Add finishing constraint: x2 <= 100/2 - x1/2
plt.plot(x1, 100/2 - x1/2, linewidth=3, label='Finishing constraint')
plt.fill_between(x1, 0, 100/2 - x1/2, alpha=0.1)

# Add carpentry constraint: x2 <= 80 - x1
plt.plot(x1, 100 - 2*x1, linewidth=3, label='Carpentry constraint')
plt.fill_between(x1, 0, 100 - 2*x1, alpha=0.1)

# Add non-negativity constraints
plt.plot(np.zeros_like(x1), x1, linewidth=3, label='$x_1$ Sign restriction')
plt.plot(x1, np.zeros_like(x1), linewidth=3, label='$x_2$ Sign restriction')

#====================================================
# This part is different from giapetto_feasible.py
# Plot the possible (x1, x2) pairs
pairs = [(x1, x2) for x1 in np.arange(101)
                for x2 in np.arange(101)
                if (x1 + 2*x2) <= 100
                and (2*x1 + x2) <= 100]

# Split these into our variables
chairs, tables = np.hsplit(np.array(pairs), 2)

# Caculate the objective function at each pair
z = 20*chairs + 30*tables

# Plot the results
plt.scatter(chairs, tables, c=z, cmap='jet', edgecolor='gray', alpha=0.5, label='Profit at each point', zorder=3)

# Colorbar
cb = plt.colorbar()
cb.set_label('Profit Colormap ($)')
#====================================================

# Labels and stuff
plt.xlabel('Chairs')
plt.ylabel('Tables')
plt.xlim(-0.5, 100)
plt.ylim(-0.5, 100)
plt.legend()
plt.show()