import numpy as np
import matplotlib.pyplot as plt
import glob

EF = 4.7935
prefix = "cspbf3.pdos"

# ==========================
# 1. BACA DATA
# ==========================
tot = np.loadtxt(f"{prefix}.pdos_tot", comments="#")
E = tot[:, 0] - EF
DOS = tot[:, 2]

Pb_s = np.zeros_like(E); Pb_p = np.zeros_like(E); Pb_d = np.zeros_like(E)
F_s = np.zeros_like(E); F_p = np.zeros_like(E)
Cs_s = np.zeros_like(E); Cs_p = np.zeros_like(E)

for file in glob.glob(f"{prefix}.pdos_atm#*"):
    data = np.loadtxt(file, comments="#")
    pdos = data[:, 2]
    if "(Pb)" in file:
        if "(s)" in file: Pb_s += pdos
        elif "(p)" in file: Pb_p += pdos
        elif "(d)" in file: Pb_d += pdos
    elif "(F)" in file:
        if "(s)" in file: F_s += pdos
        elif "(p)" in file: F_p += pdos
    elif "(Cs)" in file:
        if "(s)" in file: Cs_s += pdos
        elif "(p)" in file: Cs_p += pdos

# ==========================
# FUNGSI FORMATTING GRAFIK
# ==========================
def format_plot(ax, y_max):
    ax.axvline(0, color="black", linestyle="--", linewidth=1.0)
    ax.set_xlim(-8, 8)
    ax.set_ylim(0, y_max)
    ax.set_xlabel(r"Energy $-\,E_F$ (eV)", fontsize=14)
    ax.tick_params(axis="both", which="major", direction="in", top=True, right=True, length=6, width=1.1, labelsize=11)
    ax.tick_params(axis="both", which="minor", direction="in", top=True, right=True, length=3)
    ax.minorticks_on()
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
    ax.legend(frameon=False, fontsize=11, loc="upper right")

# ==========================
# 2. PLOT 1: TOTAL DOS
# ==========================
fig1, ax1 = plt.subplots(figsize=(7, 4))
ax1.plot(E, DOS, color="black", linewidth=1.8, label="Total DOS")
ax1.set_ylabel("Total DOS", fontsize=14)
format_plot(ax1, max(DOS) * 1.1)
ax1.text(0.2, max(DOS) * 0.9, r"$E_F$", fontsize=12, color="black")
plt.tight_layout()
plt.savefig("pdos_1_total.png", dpi=600, bbox_inches="tight")
plt.close(fig1)

# ==========================
# 3. PLOT 2: ORBITAL FLUOR (F) - Pita Valensi
# ==========================
fig2, ax2 = plt.subplots(figsize=(7, 4))
ax2.plot(E, F_s, color="#AEC7E8", linewidth=1.5, linestyle="--", label="F-s")
ax2.plot(E, F_p, color="#1F77B4", linewidth=1.5, label="F-p")
ax2.set_ylabel("F PDOS", fontsize=14)
format_plot(ax2, max(max(F_s), max(F_p)) * 1.2)
ax2.annotate("Valence band\nmainly F 2p", 
             xy=(-3.25, max(F_p)),              # <-- 100% tepat di puncak tertinggi!
             xytext=(-7.5, max(F_p) * 0.9),     # <-- Posisi teks sedikit dinaikkan agar sudutnya pas
             fontsize=12, color="#1F77B4", 
             arrowprops=dict(arrowstyle="->", color="#1F77B4"))
plt.tight_layout()
plt.savefig("pdos_2_f.png", dpi=600, bbox_inches="tight")
plt.close(fig2)

# ==========================
# 4. PLOT 3: ORBITAL TIMBAL (Pb) - Pita Konduksi
# ==========================
fig3, ax3 = plt.subplots(figsize=(7, 4))
ax3.plot(E, Pb_s, color="#FF7F0E", linewidth=1.5, label="Pb-s")
ax3.plot(E, Pb_p, color="#D62728", linewidth=1.5, label="Pb-p")
ax3.plot(E, Pb_d, color="#FFBB78", linewidth=1.5, linestyle="--", label="Pb-d")
ax3.set_ylabel("Pb PDOS", fontsize=14)
format_plot(ax3, max(max(Pb_s), max(Pb_p)) * 1.2)
ax3.annotate("Conduction band\nmainly Pb 6p", 
             xy=(3.8, max(Pb_p) * 0.98),       # Ujung panah tepat di puncak
             xytext=(0.5, max(Pb_p) * 1.35),   # Teks diangkat jauh ke atas agar tidak menabrak
             fontsize=12, color="#D62728", 
             arrowprops=dict(arrowstyle="->", color="#D62728"))
plt.tight_layout()
plt.savefig("pdos_3_pb.png", dpi=600, bbox_inches="tight")
plt.close(fig3)

# ==========================
# 5. PLOT 4: ORBITAL CESIUM (Cs)
# ==========================
fig4, ax4 = plt.subplots(figsize=(7, 4))
ax4.plot(E, Cs_s, color="#2CA02C", linewidth=1.5, label="Cs-s")
ax4.plot(E, Cs_p, color="#98DF8A", linewidth=1.5, linestyle="--", label="Cs-p")
ax4.set_ylabel("Cs PDOS", fontsize=14)
format_plot(ax4, max(max(Cs_s), max(Cs_p)) * 1.3 + 0.1)
ax4.annotate("Minor Cs\ncontribution", 
             xy=(6.6, max(Cs_s) * 0.98),       # Ujung panah di puncak
             xytext=(2.5, 1.5),                # Teks ditarik jauh ke kiri atas (y=1.5) agar panah panjang
             fontsize=12, color="#2CA02C", 
             arrowprops=dict(arrowstyle="->", color="#2CA02C"))
plt.tight_layout()
plt.savefig("pdos_4_cs.png", dpi=600, bbox_inches="tight")
plt.close(fig4)

print("Keempat grafik berhasil disimpan!")