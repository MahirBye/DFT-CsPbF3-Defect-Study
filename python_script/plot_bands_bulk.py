import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Input files and constants
# ==========================
band_file = "cspbf3.bands.dat.gnu"

VBM = 4.7935
CBM = 7.7670
Eg = CBM - VBM
nbnd = 40

# ==========================
# Load band data
# ==========================
data = np.loadtxt(band_file)

x = data[:, 0]
energy = data[:, 1] - VBM

nk = len(energy) // nbnd

x_reshaped = x.reshape((nk, nbnd), order="F")
e_reshaped = energy.reshape((nk, nbnd), order="F")

# ==========================
# High-symmetry points
# ==========================
hs_indices = [0, 20, 40, 60, 90, nk - 1]
hs_x = [x_reshaped[i, 0] for i in hs_indices]
hs_labels = [r"$\Gamma$", "X", "M", r"$\Gamma$", "R", "X"]

# ==========================
# Plot setup
# ==========================
fig, ax = plt.subplots(figsize=(7.5, 6))

ymin, ymax = -8, 8
xmin, xmax = x_reshaped.min(), x_reshaped.max()

# ==========================
# Background heatmap
# ==========================
nx = 600
ny = 600
X = np.linspace(xmin, xmax, nx)
Y = np.linspace(ymin, ymax, ny)
Z = np.zeros((ny, nx))

sigma = 0.45

for ib in range(nbnd):
    band = e_reshaped[:, ib]

    # heatmap hanya untuk band valensi
    if np.max(band) <= 0.2:
        interp_band = np.interp(X, x_reshaped[:, ib], band)
        for i in range(nx):
            Z[:, i] += np.exp(-((Y - interp_band[i]) ** 2) / (2 * sigma ** 2))

if Z.max() > 0:
    Z = Z / Z.max()

ax.imshow(
    Z,
    extent=[xmin, xmax, ymin, ymax],
    origin="lower",
    cmap="YlOrRd",
    alpha=0.65,
    aspect="auto",
    zorder=0
)

# ==========================
# Band lines
# ==========================
for ib in range(nbnd):
    ax.plot(
        x_reshaped[:, ib],
        e_reshaped[:, ib],
        color="#0033FF",
        linewidth=1.15,
        zorder=5
    )

# Fermi / VBM line
ax.axhline(0, color="black", linestyle="--", linewidth=1.0, alpha=0.8)

# Vertical high-symmetry lines
for xpos in hs_x:
    ax.axvline(xpos, color="gray", linewidth=0.9, alpha=0.8)

# ==========================
# Band gap annotation at R
# ==========================
x_R = hs_x[4]

ax.annotate(
    "",
    xy=(x_R, 0),
    xytext=(x_R, Eg),
    arrowprops=dict(arrowstyle="<->", color="black", linewidth=1.2),
    zorder=10
)

ax.text(
    x_R + 0.08,
    Eg / 2,
    rf"$E_g$ = {Eg:.2f} eV",
    fontsize=12,
    va="center",
    bbox=dict(
        boxstyle="round,pad=0.25",
        facecolor="white",
        edgecolor="black",
        linewidth=0.8
    ),
    zorder=10
)

# ==========================
# Labels and style
# ==========================
ax.set_xticks(hs_x)
ax.set_xticklabels(hs_labels, fontsize=13)

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel("Wave vector", fontsize=14)
ax.set_ylabel("Energy - VBM (eV)", fontsize=14)
ax.set_title(r"Band Structure of CsPbF$_3$", fontsize=15)

ax.tick_params(axis="y", labelsize=12)
ax.tick_params(direction="in", top=True, right=True)

plt.tight_layout()

plt.savefig("band_structure_heatmap_style.png", dpi=300)
plt.savefig("band_structure_heatmap_style.pdf")

plt.show()
