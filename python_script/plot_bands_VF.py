import numpy as np
import matplotlib.pyplot as plt

band_file = "cspbf3_VF.bands.dat.gnu"
data = np.loadtxt(band_file)

x = data[:, 0]
Eraw = data[:, 1]

# ==========================================
# 1. REFERENSI ENERGI (FERMI LEVEL)
# ==========================================
Eref = 6.8867 # Nilai mutlak dari output SCF
energy = Eraw - Eref

# ==========================================
# 2. DETEKSI OTOMATIS BANDS & K-POINTS (ANTI-GAGAL)
# ==========================================
# Mencari di indeks mana sumbu X me-reset (anjlok) kembali ke 0
drop_indices = np.where(np.diff(x) < 0)[0]
if len(drop_indices) > 0:
    nk = drop_indices[0] + 1
else:
    nk = len(x)

nbnd = len(x) // nk

print(f"Data terbaca! Ditemukan: {nbnd} pita energi (bands) dan {nk} titik k (k-points).")

# Reshape data
x_reshaped = x.reshape((nk, nbnd), order="F")
e_reshaped = energy.reshape((nk, nbnd), order="F")

# ==========================================
# 3. PLOTTING BAND STRUCTURE
# ==========================================
hs_indices = [0, 10, 20, 30, 40, nk - 1]
hs_x = [x_reshaped[i, 0] for i in hs_indices]
hs_labels = [r"$\Gamma$", "X", "M", r"$\Gamma$", "R", "X"]

fig, ax = plt.subplots(figsize=(7.5, 6))

# Plot semua bands
for ib in range(nbnd):
    ax.plot(
        x_reshaped[:, ib],
        e_reshaped[:, ib],
        color="#0033FF",
        linewidth=1.15
    )

# Garis referensi Fermi (0 eV)
ax.axhline(0, color="black", linestyle="--", linewidth=1.2)

for xpos in hs_x:
    ax.axvline(xpos, color="gray", linewidth=0.9, alpha=0.8)

ax.set_xticks(hs_x)
ax.set_xticklabels(hs_labels, fontsize=13)

ax.set_xlim(x_reshaped.min(), x_reshaped.max())

# Batas sumbu Y difokuskan ke celah pita
ax.set_ylim(-4.5, 4.5) 

ax.set_xlabel("Wave vector", fontsize=14)
ax.set_ylabel(r"Energy $-\,E_F$ (eV)", fontsize=14)
ax.set_title(r"Band Structure of CsPbF$_3$ with $V_F$", fontsize=15)

ax.tick_params(axis="y", labelsize=12)
ax.tick_params(direction="in", top=True, right=True)

plt.tight_layout()

# Simpan hasil grafik yang benar
plt.savefig("band_structure_VF_final.png", dpi=300)
plt.savefig("band_structure_VF_final.pdf")

plt.show()