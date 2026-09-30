# AGENTS.md — Context & Instruction Handbook for AI Agents
> **Workspace:** `Workspace-MP-PRE-02`  
> **Tujuan:** Panduan instruksi komprehensif, konteks penelitian, standar penulisan akademis, dan panduan operasional teknis agar setiap AI Agent (Claude, ChatGPT, Gemini, Cursor, Copilot, Antigravity, dll.) dapat langsung melanjutkan pengerjaan proyek dan perkuliahan ini tanpa kehilangan konteks sedikit pun.

---

## 1. Identitas Akademik & Kepemilikan Proyek

Bila Anda bertindak sebagai AI Agent di workspace ini, Anda mendampingi mahasiswa berikut dalam penyusunan tugas akademis dan riset manajemen proyek:

* **Nama Mahasiswa:** Muhammad Nailul Ghufron Majid
* **NIM:** 240605110160
* **Mata Kuliah:** Teori Manajemen Proyek (Tahun Akademik 2026)
* **Dosen Pengampu:** Dr. Muhammad Ainul Yaqin, S.Si, M.Kom
* **Program Studi:** S1 Teknik Informatika
* **Fakultas:** Sains dan Teknologi
* **Perguruan Tinggi:** Universitas Islam Negeri Maulana Malik Ibrahim Malang
* **Tahun:** 2026

---

## 2. Profil Penelitian & Proyek Terintegrasi (PRE-02)

Seluruh Lembar Kerja Mahasiswa (LKM) individu maupun tugas kelompok diintegrasikan dengan proyek riset kelompok berkode **PRE-02**. Dokumen detail riset tersimpan pada folder `judul_dan_progres_penelitian/`.

### A. Judul & Esensi Proyek
* **Judul Resmi:** *Sistem Prediksi Probabilitas Keterlambatan Proyek Berbasis Machine Learning sebagai Early Warning System Manajemen Proyek*
* **Kode Proyek Kelompok:** PRE-02
* **Problem Statement:** Klasifikasi biner konvensional (terlambat vs tepat waktu) hanya menghasilkan label diskrit tanpa gradasi kepastian. Proyek PRE-02 membangun model yang menghasilkan **probabilitas numerik kontinu $[0.0 - 1.0]$ yang terkalibrasi**, sehingga berfungsi sebagai sistem peringatan dini (*Early Warning System*) berbasis risiko bagi Manajer Proyek.

### B. Variabel Penelitian (Features & Target)
* **Variabel Bebas / Features (7 Parameter Kondisi Proyek pada Tahap Monitoring):**
  1. *Progres Aktual vs Rencana:* Selisih persentase realisasi pekerjaan terhadap jadwal baseline.
  2. *Sisa Waktu Deadline:* Jumlah hari kalender tersisa hingga tanggal target penyelesaian.
  3. *Sisa Backlog:* Jumlah *story points* atau *tasks* yang belum tuntas.
  4. *Tingkat Utilisasi SDM:* Beban kerja tim pengembang (rasio alokasi vs kapasitas normal).
  5. *Jumlah Risiko Aktif:* Total risiko teridentifikasi yang belum selesai dimitigasi.
  6. *Frekuensi Perubahan (Change Requests):* Jumlah permintaan perubahan ruang lingkup yang diajukan.
  7. *Dependency Score:* Nilai bobot ketergantungan tugas terhadap modul/tim eksternal.
* **Variabel Terikat / Target:**
  * Probabilitas keterlambatan numerik kontinu $[0.0 - 1.0]$ yang dihasilkan oleh fungsi aktivasi sigmoid/predict_proba terkalibrasi.

### C. Desain Eksperimen & Algoritma Machine Learning
1. **Model Baseline:** *Logistic Regression* (probabilitas dasar terkalibrasi secara alami).
2. **Model Ensemble Tree:** *Random Forest* dengan `predict_proba`.
3. **Model Boosting:** *Gradient Boosting* (XGBoost / LightGBM) dengan `predict_proba`.
4. **Model Deep Learning:** *Neural Network Multi-Layer Perceptron (MLP)* dengan output aktivasi Sigmoid.
5. **Kalibrasi Probabilitas:** Penerapan *Platt Scaling* (metode sigmoid) dan *Isotonic Regression* untuk mereduksi *Expected Calibration Error* (ECE).
6. **Ambang Batas Peringatan Dini (Threshold Alert):** Default $\ge 0.65$ untuk memicu sinyal bahaya keterlambatan.

### D. Metrik Evaluasi Kinerja Model
* **Brier Score:** Mengukur akurasi kuadratik dari estimasi probabilitas (target $< 0.18$).
* **Log Loss / Cross-Entropy:** Mengukur penalti ketidakpastian probabilitas.
* **Area Under ROC Curve (AUC-ROC):** Mengukur kemampuan diskriminasi model (target $\ge 0.80$).
* **Calibration Curve & Expected Calibration Error (ECE):** Memvalidasi seberapa dekat probabilitas terprediksi dengan frekuensi empiris aktual.

---

## 3. Peta Kemajuan Perkuliahan (Syllabus & LKM Tracking)

| Pertemuan | Topik LKM | Status Dokumen | Lokasi File Output (.docx) | Lokasi Script Generator |
|---|---|---|---|---|
| **Pertemuan 1** | Pengantar Manajemen Proyek | ✅ **SELESAI** | `MP_Tugas_Individu/LKM1_Manajemen_Proyek.docx` | Manual / Archive |
| **Pertemuan 2** | Lingkungan Proyek & Peran PM | ✅ **SELESAI** | `MP_Tugas_Individu/LKM2_Manajemen_Proyek.docx` | Manual / Archive |
| **Pertemuan 3** | Manajemen Integrasi Proyek | ✅ **SELESAI** | `MP_Tugas_Individu/LKM3_Manajemen_Proyek.docx` | `scripts/lkm3/generate_lkm3_final.py` |
| **Pertemuan 4** | Manajemen Ruang Lingkup Proyek | ✅ **SELESAI** | `MP_Tugas_Individu/LKM4_Manajemen_Proyek.docx` | `scripts/lkm4/generate_lkm4_final.py` |
| **Pertemuan 5** | Manajemen Jadwal Proyek (Bagian I) | ⏳ **BERIKUTNYA** | `MP_Tugas_Individu/LKM5_Manajemen_Proyek.docx` | `scripts/lkm5/` *(Buat saat tiba tugas)* |
| **Pertemuan 6** | Manajemen Jadwal (II) & Biaya | ⏳ Antrean | `MP_Tugas_Individu/LKM6_Manajemen_Proyek.docx` | `scripts/lkm6/` |
| **Pertemuan 7** | Analisis Data & Pembahasan Riset | ⏳ Antrean | `MP_Tugas_Individu/LKM7_Manajemen_Proyek.docx` | `scripts/lkm7/` |
| **Pertemuan 8** | Finalisasi Paper IMRAD & Presentasi | ⏳ Antrean | `MP_Tugas_Individu/LKM8_Manajemen_Proyek.docx` | `scripts/lkm8/` |

---

## 4. Tata Kelola & Struktur Direktori Workspace

Workspace ini dirancang dengan struktur terorganisir:

```
c:/Users/nailul/Documents/Files_Kuliah_Local/Workspace-MP-PRE-02/
├── AGENTS.md                               # Dokumen ini (Handbook & Instruksi Agen AI)
├── uin_logo.png                            # Logo resmi UIN Malang untuk cover dokumen Word
├── [PMI]_PMBOK-6th_ed-2017(b-ok.xyz).pdf   # Buku rujukan primer PMI (PMBOK Guide Edisi 6)
├── Project_Management_ The_Managerial_Process.pdf # Buku rujukan primer Larson & Gray (Edisi 8)
│
├── MP_Tugas_Individu/                      # DIREKTORI OUTPUT UTAMA FILE DOCX LKM
│   ├── LKM1_Manajemen_Proyek.docx
│   ├── LKM2_Manajemen_Proyek.docx
│   ├── LKM3_Manajemen_Proyek.docx
│   └── LKM4_Manajemen_Proyek.docx
│
├── MP_sumber_data/                         # DIREKTORI SILABUS & SOAL SUMBER
│   └── 2026 Lembar Kerja Mahasiswa_Manajemen_Proyek_Revisi_v3.docx
│
├── judul_dan_progres_penelitian/           # DOKUMEN RISET KELOMPOK PRE-02
│   ├── Deskripsi_Penelitian.md             # Spesifikasi model ML & variabel penelitian
│   └── progres_penelitian_MP.md            # Rencana roadmap 8 pertemuan riset
│
└── scripts/                                # DIREKTORI SELURUH SKRIP EKSEKUSI & GENERATOR
    ├── run_generator.py                    # Master Runner (bisa generate LKM tertentu atau all)
    ├── lkm4/                               # Modul Generator LKM 4
    │   ├── generate_lkm4_final.py          # Script utama LKM 4
    │   ├── lkm4_builder_section_a.py       # Builder Tugas Tertulis (10 Soal + Matriks RTM)
    │   ├── lkm4_builder_section_b.py       # Builder Refleksi Mandiri (5 Soal)
    │   └── lkm4_builder_section_c.py       # Builder Daftar Pustaka APA 7th
    ├── lkm3/                               # Modul Generator LKM 3
    │   ├── generate_lkm3_final.py          # Script utama LKM 3
    │   ├── section_a_builder.py            # Builder Tugas Tertulis (8 Soal)
    │   ├── section_c_builder.py            # Builder Ringkasan PMBOK Bab 4.1-4.2
    │   └── section_d_e_builder.py          # Builder Refleksi & Daftar Pustaka
    └── utils/                              # Alat utilitas pendukung
        └── inspect_docx.py                 # Script pengecekan struktur/paragraf docx
```

---

## 5. Standar Format Dokumen Akademis Word (`.docx`)

Setiap dokumen LKM yang dibuat harus memenuhi parameter ketat berikut agar seragam dengan dokumen sebelumnya:

### A. Pengaturan Halaman (Page Setup)
* **Ukuran Kertas:** A4 ($21.0\text{ cm} \times 29.7\text{ cm}$).
* **Margin:** Standar penulisan karya ilmiah Indonesia, yaitu **3.0 cm pada keempat sisi** (*Top: 3.0 cm, Bottom: 3.0 cm, Left: 3.0 cm, Right: 3.0 cm*).

### B. Tipografi & Hierarki Gaya (Styles)
* **Font Family:** Seluruh elemen teks menggunakan **Times New Roman**.
* **Heading 1:** Ukuran 14 pt, **Bold**, warna Hitam, Spasi Sebelum 16 pt, Spasi Sesudah 9 pt, Line Spacing 1.15.
* **Heading 2:** Ukuran 12 pt, **Bold**, warna Hitam, Spasi Sebelum 12 pt, Spasi Sesudah 5 pt, Line Spacing 1.15.
* **Heading 3:** Ukuran 12 pt, **Bold + Italic**, warna Hitam, Spasi Sebelum 8 pt, Spasi Sesudah 4 pt, Line Spacing 1.15.
* **Teks Isi (Body Paragraph):** Ukuran 12 pt, Regular, warna Hitam, Line Spacing **1.5**, Spasi Sesudah 6 pt, Perataan **Justify (Rata Kanan-Kiri)**.
* **Daftar Bernomor & Poin (Num/Bullet):** Left Indent 0.25 inci, Spasi Sesudah 4 pt, Line Spacing 1.5, perataan Justify.
* **Sub-poin / Sub-bullet:** Left Indent 0.45 inci, simbol dash (`–`), Spasi Sesudah 4 pt, Line Spacing 1.5.

### C. Standar Desain Tabel Akademis
* **Alignment:** Rata Tengah (*Center*).
* **Borders:** Garis tunggal tipis rapi (*single line*, border color `#000000` atau subtle dark grey).
* **Header Baris Pertama:**
  * Background shading: Soft slate/ice blue `#E8EEF5`.
  * Teks: Times New Roman 11 pt, **Bold**, Center, Line Spacing 1.15.
  * Dilengkapi tag XML `<w:tblHeader>` agar berulang di setiap halaman jika tabel terpotong.
* **Sel Data:**
  * Teks: Times New Roman 10 pt atau 11 pt, Regular, Line Spacing 1.15.
  * Cell Margins (Padding): Top 100 dxa, Bottom 100 dxa, Left 150 dxa, Right 150 dxa.
  * Dilengkapi tag XML `<w:cantSplit>` pada setiap baris untuk mencegah teks terbelah antartitik halaman.

### D. Format Halaman Sampul (Cover Page)
Cover diletakkan pada halaman pertama yang diakhiri *Page Break*, memuat secara berurutan:
1. Judul LKM (Contoh: `LKM 4: MANAJEMEN RUANG LINGKUP PROYEK`), 12 pt, Bold, Center.
2. `Mata Kuliah: Teori Manajemen Proyek`, 11 pt, Center.
3. `Dosen Pengampu: Dr. Muhammad Ainul Yaqin, S.Si, M.Kom`, 12 pt, Bold, Center.
4. Logo resmi UIN Malang (`uin_logo.png`, lebar presisi $4.85\text{ cm}$), Center.
5. `Oleh :`
6. `Muhammad Nailul Ghufron Majid` (12 pt, Center).
7. `240605110160` (12 pt, Center).
8. Instansi penutup (12 pt, Bold, Center):
   * `PRODI TEKNIK INFORMATIKA`
   * `FAKULTAS SAINS DAN TEKNOLOGI`
   * `UNIVERSITAS ISLAM NEGERI MAULANA MALIK IBRAHIM`
   * `MALANG`
   * `2026`

---

## 6. Standar Kualitas Jawaban & Metodologi Penulisan

Bagi AI Agent yang menyusun tugas LKM berikutnya:
1. **Rujukan Teori Internasional yang Wajib Digunakan:**
   * *PMBOK® Guide 6th Edition (PMI, 2017/2018):* Bab yang relevan dengan topik pertemuan.
   * *Project Management: The Managerial Process (Larson & Gray, 2021).*
   * *Information Technology Project Management (Schwalbe, 2019).*
   * *Project Management: A Systems Approach to Planning, Scheduling, and Controlling (Kerzner, 2017).*
2. **Karakter Jawaban:**
   * Jangan memberikan jawaban ringkas, dangkal, atau sekadar poin-poin singkat tanpa elaborasi.
   * Setiap jawaban konseptual harus diuraikan secara mendalam, analitis, logis, dan profesional dengan perspektif akademisi Teknik Informatika.
   * Berikan perbandingan tabel komparatif jika pertanyaan menanyakan perbedaan dua atau lebih konsep (misal: *Validate Scope vs Control Scope*, *CPM vs PERT*, dll.).
3. **Kontekstualisasi ke Proyek PRE-02:**
   * Pertanyaan yang meminta contoh riil proyek kelompok, daftar kebutuhan, WBS, jadwal, atau refleksi mandiri **WAJIB dihubungkan secara konsisten dengan proyek PRE-02** (Prediksi Probabilitas Keterlambatan Proyek Berbasis Machine Learning sebagai Early Warning System).
4. **Daftar Pustaka:**
   * Setiap LKM wajib menyertakan bagian akhir Daftar Pustaka yang disusun rapi menggunakan format **APA 7th Edition** dengan *hanging indent*.

---

## 7. Panduan Perintah Eksekusi (Quick Start Commands)

Setiap script Python di workspace ini dirancang dengan resolusi path dinamis (`find_workspace_root`), sehingga aman dieksekusi dari direktori mana pun.

```bash
# ==============================================================================
# CARA MENJALANKAN GENERATOR DOKUMEN WORD (.DOCX)
# ==============================================================================

# 1. Menjalankan Master Runner untuk LKM tertentu:
python scripts/run_generator.py --lkm 4
python scripts/run_generator.py --lkm 3

# 2. Menjalankan Master Runner untuk seluruh dokumen:
python scripts/run_generator.py --all

# 3. Menjalankan script modul LKM langsung:
python scripts/lkm4/generate_lkm4_final.py
python scripts/lkm3/generate_lkm3_final.py

# 4. Melakukan inspeksi dokumen Word yang telah digenerate:
python scripts/utils/inspect_docx.py
```

---

## 8. Panduan Langkah Pembuatan LKM Selanjutnya (Contoh: LKM 5)

Ketika pengguna meminta: *"Kerjakan LKM Pertemuan 5"*, ikuti langkah kerja sistematis berikut:

1. **Analisis Soal Sumber:**
   * Ekstrak teks silabus Pertemuan 5 dari `MP_sumber_data/2026 Lembar Kerja Mahasiswa_Manajemen_Proyek_Revisi_v3.docx`.
   * Identifikasi seluruh soal Tugas Tertulis Individu, Tugas Khusus/Jadwal, Refleksi Mandiri, dan Catatan Dosen.
2. **Buat Direktori Script Baru:**
   * Buat folder `scripts/lkm5/`.
   * Buat builder modular:
     * `lkm5_builder_section_a.py` (Tugas Tertulis Individu seputar Manajemen Jadwal: Activity Definition, Sequencing, Duration Estimating, Critical Path Method / PDM).
     * `lkm5_builder_section_b.py` (Refleksi Mandiri kontekstual PRE-02).
     * `lkm5_builder_section_c.py` (Daftar Pustaka APA 7th).
     * `generate_lkm5_final.py` (Main orchestrator penyusun docx).
3. **Daftarkan ke Master Runner:**
   * Tambahkan entri `"5"` ke dictionary `LKM_SCRIPTS` di `scripts/run_generator.py`.
4. **Eksekusi & Verifikasi Output:**
   * Jalankan `python scripts/lkm5/generate_lkm5_final.py`.
   * Pastikan file `MP_Tugas_Individu/LKM5_Manajemen_Proyek.docx` terbentuk dengan sempurna, format rapi, tabel valid, dan tanpa error.
