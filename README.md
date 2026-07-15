# DFT-CsPbF3-Defect-Study

# Studi Komputasi First-Principles: Sifat Elektronik CsPbF3 dan Cacat _Vacancy_ Fluorin (VF)

Repositori ini memuat seluruh data komputasi *Density Functional Theory* (DFT) dan skrip pemrosesan data (Python) yang digunakan dalam penelitian tugas akhir/skripsi mengenai evaluasi sifat elektronik material perovskit halida anorganik $CsPbF_3$.

Penelitian ini membandingkan struktur kristal, struktur pita energi (*Band Structure*), dan *Partial Density of States* (PDOS) antara $CsPbF_3$ fasa *bulk* murni dan *supercell* $2 \times 2 \times 2$ yang mengandung cacat intrinsik berupa kekosongan atom Fluorin ($V_F$).

## 🛠️ Perangkat Lunak yang Digunakan
* **Quantum ESPRESSO (QE):** Digunakan untuk seluruh tahap kalkulasi (Relaksasi, SCF, Bands, DOS, dan PDOS) dengan fungsional pertukaran-korelasi GGA-PBE.
* **VESTA:** Digunakan untuk memodelkan *supercell*, relaksasi visual, dan mengekstrak koordinat fraksional atom.
* **Python 3:** Digunakan untuk mengolah dan memvisualisasikan data keluaran komputasi.

## 📂 Struktur Repositori

```text
├── bulk/                             # Data komputasi CsPbF3 fasa ideal murni
│   ├── relax/
│   │   └── cspbf3_vc-relax.in        # Skrip optimasi geometri sel satuan
│   ├── scf/
│   │   └── cspbf3_scf_final.in       # Skrip kalkulasi Self-Consistent Field
│   ├── bands/
│   │   └── cspbf3_bands.in           # Skrip struktur pita energi
│   ├── dos/
│   │   ├── cspbf3_nscf.in            # Skrip Non-SCF
│   │   └── dos.in                    # Skrip kalkulasi Total DOS
│   └── pdos/
│       └── pdos.in                   # Skrip dekonvolusi orbital (PDOS)
│
├── defect/                           # Data komputasi fasa cacat VF (Supercell)
│   ├── scf/
│   │   └── cspbf3_VF_scf.in          # Skrip SCF untuk supercell 39 atom
│   ├── bands/
│   │   └── cspbf3_VF_bands_retry.in  # Skrip struktur pita energi cacat
│   ├── dos/                          
│   │   └── [File dalam proses pembaruan]
│   └── pdos/
│       └── pdos_VF.in                # Skrip kalkulasi PDOS cacat
│
├── python_script/                    # Kumpulan skrip pemrograman visualisasi
│   ├── plot_bands_bulk.py            # Skrip kurva pita energi Bulk
│   ├── plot_bands_VF.py              # Skrip kurva pita energi Defect
│   ├── plot_dos_pdos_bulk.py         # Skrip visualisasi DOS/PDOS Bulk
│   └── plot_dos_pdos_VF.py           # Skrip visualisasi DOS/PDOS Defect
│
└── structures/                       # Data kristalografi koordinat atom
    ├── cspbf3_initial.cif            # CIF awal CsPbF3
    ├── cspbf3_relaxed.cif            # CIF hasil optimasi vc-relax
    └── cspbf3_VF_2x2x2.cif           # CIF fasa cacat dari VESTA
```

## 👨‍🔬 Penulis
**Muhamad Habbiebie Robbi** | Program Studi Fisika  
Universitas Negeri Jakarta  

Repositori ini didedikasikan untuk menjunjung tinggi transparansi data riset (Open Science) serta sebagai prasyarat pemenuhan bagian Lampiran pada Naskah Skripsi.
