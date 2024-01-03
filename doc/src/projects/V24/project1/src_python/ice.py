#%%
import rockhound as rh
import matplotlib.pyplot as plt
import cmocean
import numpy as np

bedmap = rh.fetch_bedmap2(datasets=["thickness","surface","bed"])
plt.figure(figsize=(8, 7))
ax = plt.subplot(111)
bedmap.surface.plot.pcolormesh(ax=ax,cmap=cmocean.cm.ice,
                       cbar_kwargs=dict(pad=0.01, aspect=30))
plt.title("Bedmap2 Antarctica")
plt.tight_layout()
plt.show()
# %%
plt.close()
ax = plt.subplot(111)
bedmap.thickness.plot.pcolormesh(ax=ax,cmap=cmocean.cm.ice,
                       cbar_kwargs=dict(pad=0.01, aspect=30))
plt.show()
# %%
import rockhound as rh
import matplotlib.pyplot as plt
import cmocean

# Load the age and uncertainty grids in the default 6 arc-minute resolution
grid = rh.fetch_seafloor_age()
print(grid)

# Plot the age grid.
# We're not using a map projection to speed up the plotting but this NOT
# recommended.
plt.figure(figsize=(9, 5))
ax = plt.subplot(111)
grid.age.plot.pcolormesh(
    cmap=cmocean.cm.thermal_r, cbar_kwargs=dict(pad=0.01, aspect=30), ax=ax
)
ax.set_title("Age of Oceanic Lithosphere")
plt.tight_layout()
plt.show()
# %%
