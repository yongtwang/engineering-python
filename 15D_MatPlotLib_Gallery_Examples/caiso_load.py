"""
Plot the CAISO hourly load data in 3D.
[J15] Wang, Y., Li, L. (2016). Critical peak electricity pricing for sustainable manufacturing: Modeling and case studies. Applied Energy, 175, 40-53.
https://www.binghamton.edu/centers/seorl/publications.html
"""
import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# Read the load data.
year = 2012
mat = list()
f = open('caiso_load_{}.csv'.format(year))
rows = csv.reader(f)
for row in rows:
    # print(row)
    mat.append(row)
f.close()
mat=np.array(mat)
xnum, ynum = np.shape(mat)
#print('xnum =', xnum)  #for debugging
#input("Press Enter to continue...")
#print('ynum =', ynum)
#input("Press Enter to continue...")

X = np.arange(1, xnum)
Y = np.arange(1, ynum)
Y, X = np.meshgrid(Y, X)
Z = mat[1:, 1:]
Z = Z.astype(float) # Revised on 11/7/2023


# Plot the data.
fig = plt.figure(figsize=(9, 3))
ax = fig.add_axes([-0.12, 0.0, 1.22, 1.10],
                  projection='3d')

cmap = mpl.colors.ListedColormap(["#efe8f2",
                                  "#c2a5cf",
                                  "#7b3294"])
#cmap = mpl.colors.ListedColormap(["g","b","r"])
bounds = np.max(Z) * np.array([0, 0.6, 0.9, 1])
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
surf = ax.plot_surface(X, Y, Z, rstride=1,
                       cstride=1, cmap=cmap,
                       norm=norm, linewidth=0.1, edgecolor='k',
                       antialiased=True, alpha=0.9)

ax.set_zlabel('Load (MW)')
ax.set_xlim(0, xnum-1)
ax.set_ylim(0, ynum-1)
ax.set_zlim(0.1, np.max(Z)) #to avoid overlapping
ax.view_init(azim=-80, elev=30)


# Fine tune the x and y tick labels.
# Find the start of each month.
loc = np.zeros(12)
labels = np.array(['']*12, dtype='U10')
date = mat[1:, 0]
j = 0
for i in range(0, len(date)):
    if '/1/'+str(year) in date[i]:
        loc[j] = i
        labels[j] = date[i]
        j = j + 1
ax.set_xticks(loc)
ax.set_xticklabels(labels, rotation=15,
                   verticalalignment='center')

loc = np.arange(0, 25, 4)
labels = loc.astype('str')
ax.set_yticks(loc)
ax.set_yticklabels(labels, rotation=0,
                   verticalalignment='center')


# Add the colorbar.
cax = fig.add_axes([0.03, 0.2, 0.01, 0.5])
cbar = plt.colorbar(surf, cax=cax, ax=ax,
                    cmap=cmap, norm=norm,
                    ticks=bounds,
                    spacing='proportional',
                    orientation='vertical')
cbar.ax.set_yticklabels(['0', '60', '90', '100'])
cbar.set_label('% of peak load', labelpad=-50)


# Calculate hours with load > 90% of peak load.
hours = Z[Z>bounds[2]].size
percent = hours / Z.size * 100
print('Hours with load >90%: {0}, which is {1:0.2f}%.'
      .format(hours, percent))

# Show and save the figure.
fig.savefig('caiso_load.png', dpi=200)
plt.show()
