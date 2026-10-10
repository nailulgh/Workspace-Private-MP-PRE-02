# -*- coding: utf-8 -*-
"""
Section B Builder: Tugas Latihan & Studi Kasus Individu
Pertemuan 13: Analisis Make-or-Buy dan Stakeholder Mapping Proyek PRE-02
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_b(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_heading_2 = helpers['add_heading_2']
    add_heading_3 = helpers['add_heading_3']
    add_body_p = helpers['add_body_p']
    add_num_p = helpers['add_num_p']
    add_bullet_p = helpers['add_bullet_p']
    add_subbullet_p = helpers['add_subbullet_p']
    create_table = helpers['create_table']

    add_heading_1(doc, "B. TUGAS LATIHAN DAN STUDI KASUS INDIVIDU: ANALISIS PENGADAAN MAKE-OR-BUY DAN STAKEHOLDER MAPPING")

    add_body_p(doc,
        "Untuk mengoperasionalkan konsep manajemen pengadaan dan manajemen pemangku kepentingan secara aplikatif, "
        "tugas individu ini menyajikan simulasi analisis pengadaan Make-or-Buy berbasis titik impas (Break-Even Analysis) "
        "serta pemetaan visual Power/Interest Grid pada proyek riset PRE-02 (Sistem Prediksi Probabilitas Keterlambatan "
        "Proyek Berbasis Machine Learning sebagai Early Warning System):")

    # =========================================================================
    # STUDI KASUS 1: ANALISIS KUANTITATIF MAKE-OR-BUY INFRASTRUKTUR KOMPUTASI
    # =========================================================================
    add_heading_2(doc, "1. Studi Kasus Kuantitatif Analisis Make-or-Buy: Pengadaan Infrastruktur Server Komputasi Model ML")
    add_body_p(doc,
        "Konteks Skenario: Dalam melatih algoritma Machine Learning yang kompleks (Neural Network MLP, Random Forest, dan Gradient Boosting) "
        "serta melakukan kalibrasi probabilitas berulang (Platt Scaling dan Isotonic Regression), tim proyek PRE-02 membutuhkan daya komputasi GPU "
        "yang andal. Tim dihadapkan pada dua opsi akuisisi:")
    
    add_bullet_p(doc, "Opsi 1 (Make / Bangun Server On-Premise Mandiri): Membeli unit workstation PC dengan kartu grafis GPU khusus kelas workstation (Nvidia RTX 4090) seharga Rp 45.000.000 (biaya modal tetap awal / Fixed Cost). Biaya operasional bulanan (listrik, pendingin lab, dan pemeliharaan rutin) diestimasi sebesar Rp 500.000 per bulan.")
    add_bullet_p(doc, "Opsi 2 (Buy / Sewa Layanan Cloud GPU Terkelola - e.g., RunPod / AWS EC2 G5): Tidak ada biaya investasi awal (Fixed Cost = Rp 0). Biaya sewa komputasi cloud berbasis langganan fleksibel diestimasi sebesar Rp 3.500.000 per bulan (Variable Cost).")

    add_heading_3(doc, "a. Perhitungan Titik Impas (Break-Even Analysis)")
    add_body_p(doc,
        "Persamaan total biaya kedua opsi dirumuskan sebagai fungsi dari durasi proyek dalam bulan (M):")
    add_bullet_p(doc, "Total Biaya Make: TC(Make) = Biaya Tetap + (Biaya Variabel per Bulan × M) = Rp 45.000.000 + (Rp 500.000 × M)")
    add_bullet_p(doc, "Total Biaya Buy: TC(Buy) = Biaya Tetap + (Biaya Variabel per Bulan × M) = Rp 0 + (Rp 3.500.000 × M)")
    
    add_body_p(doc,
        "Titik impas (Break-Even Month / M*) tercapai saat TC(Make) = TC(Buy):")
    add_bullet_p(doc, "Rp 45.000.000 + Rp 500.000 × M = Rp 3.500.000 × M")
    add_bullet_p(doc, "Rp 45.000.000 = (Rp 3.500.000 - Rp 500.000) × M")
    add_bullet_p(doc, "Rp 45.000.000 = Rp 3.000.000 × M")
    add_bullet_p(doc, "M* = Rp 45.000.000 / Rp 3.000.000 = 15 Bulan")

    add_heading_3(doc, "b. Evaluasi Keputusan Berdasarkan Durasi Proyek PRE-02")
    add_body_p(doc,
        "Riset proyek PRE-02 dirancang untuk diselesaikan dalam durasi 1 semester perkuliahan aktif (4 bulan durasi intensif eksekusi eksperimen). "
        "Perbandingan biaya total pada M = 4 bulan adalah:")
    add_bullet_p(doc, "TC(Make pada 4 bulan) = Rp 45.000.000 + (Rp 500.000 × 4) = Rp 47.000.000")
    add_bullet_p(doc, "TC(Buy pada 4 bulan) = Rp 3.500.000 × 4 = Rp 14.000.000")
    add_bullet_p(doc, "Selisih Penghematan Finansial: Rp 47.000.000 - Rp 14.000.000 = Rp 33.000.000 (Opsi Buy menghemat 70,21% anggaran).")

    add_body_p(doc,
        "Keputusan Akhir Pengadaan: OPSI BUY (SEWA CLOUD GPU) DIREKOMENDASIKAN.\n"
        "Justifikasi Strategis:\n"
        "Karena durasi kebutuhan komputasi proyek (4 bulan) jauh berada di bawah titik impas (15 bulan), membeli workstation fisik mandiri "
        "merupakan pemborosan modal (capital expenditure) yang sangat tidak efisien. Opsi Buy menghilangkan risiko kerusakan perangkat keras, "
        "meniadakan depresiasi aset pasca-proyek selesai, dan memberikan skalabilitas kapasitas on-demand yang langsung siap pakai.")

    headers_mob = ["Dimensi Evaluasi", "Opsi Make (Beli Server Fisik)", "Opsi Buy (Sewa Cloud GPU)", "Analisis Komparatif"]
    data_mob = [
        ["Biaya Tetap Awal (Fixed Cost)", "Rp 45.000.000 (Sangat Tinggi)", "Rp 0 (Nol Investasi)", "Buy unggul mutlak pada fase inisiasi."],
        ["Biaya Operasional (per bulan)", "Rp 500.000 / bulan", "Rp 3.500.000 / bulan", "Make lebih murah jika digunakan > 15 bulan."],
        ["Total Biaya untuk 4 Bulan", "Rp 47.000.000", "Rp 14.000.000", "Buy menghemat Rp 33.000.000 (70,2%)."],
        ["Fleksibilitas & Skalabilitas", "Kapasitas terkunci pada spesifikasi GPU tetap.", "Bebas upgrade instance GPU kapan saja sesuai kebutuhan.", "Buy memberikan agilitas rekayasa data science."],
        ["Rekomendasi Keputusan", "DITOLAK", "DIPILIH (SEWA CLOUD)", "Pilihan optimal untuk durasi proyek akademik."]
    ]
    create_table(doc, headers_mob, data_mob)

    # =========================================================================
    # STUDI KASUS 2: PEMETAAN STAKEHOLDER MATRIX & POWER/INTEREST GRID
    # =========================================================================
    add_heading_2(doc, "2. Pemetaan Pemangku Kepentingan (Stakeholder Mapping) Proyek PRE-02")
    add_body_p(doc,
        "Berdasarkan analisis ruang lingkup dan lingkungan organisasi proyek riset PRE-02, diidentifikasi tujuh pemangku kepentingan "
        "kunci yang kemudian dipetakan ke dalam Power/Interest Grid 2 × 2:")

    headers_reg = ["ID", "Nama / Peran Stakeholder", "Posisi / Organisasi", "Kekuasaan (Power)", "Kepentingan (Interest)", "Penempatan Kuadran", "Strategi Utama Keterlibatan"]
    data_reg = [
        [
            "SH-01",
            "Dr. Muhammad Ainul Yaqin, M.Kom\n(Dosen Pengampu / Sponsor)",
            "Dosen Pengampu Mata Kuliah / Fakultas Saintek",
            "Tinggi",
            "Tinggi",
            "Kuadran I:\nManage Closely",
            "Rapat asistensi berkala, pelaporan progres milestone LKM, dan konsultasi arah metodologi ML secara proaktif."
        ],
        [
            "SH-02",
            "Muhammad Nailul Ghufron Majid\n(Project Manager / ML Lead)",
            "Mahasiswa / Tim Pengembang Internal",
            "Tinggi",
            "Tinggi",
            "Kuadran I:\nManage Closely",
            "Memimpin koordinasi harian, memantau baseline jadwal dan biaya, serta mengambil keputusan arsitektur teknis."
        ],
        [
            "SH-03",
            "Tim Pengembang Mahasiswa\n(Data Scientist & Backend Dev)",
            "Anggota Tim Peneliti / Internal Kampus",
            "Tinggi",
            "Tinggi",
            "Kuadran I:\nManage Closely",
            "Sprint meeting harian, peer code review di GitHub, dan penyelarasan kontrak interface API secara transparan."
        ],
        [
            "SH-04",
            "Ketua Program Studi Teknik Informatika\n(Pimpinan Akademik)",
            "Program Studi S1 TI UIN Malang",
            "Tinggi",
            "Rendah",
            "Kuadran II:\nKeep Satisfied",
            "Penyampaian laporan ringkasan mutu kurikulum, menjaga kepatuhan terhadap standar etika akademik kampus."
        ],
        [
            "SH-05",
            "Kepala Laboratorium Komputasi\n(Penyedia Fasilitas Lab)",
            "Unit Laboratorium Terpadu Fakultas",
            "Tinggi",
            "Rendah",
            "Kuadran II:\nKeep Satisfied",
            "Mematuhi SOP penggunaan jaringan kampus, mengamankan alokasi bandwidth, dan menjaga kebersihan sarana lab."
        ],
        [
            "SH-06",
            "Praktisi / Manajer Proyek TI Eksternal\n(Calon Pengguna Akhir)",
            "Industri Software House / Mitra Pengguna",
            "Rendah",
            "Tinggi",
            "Kuadran III:\nKeep Informed",
            "Sesi wawancara kebutuhan sistem peringatan dini, showcase demo prototipe, dan pengumpulan kuesioner kegunaan UI."
        ],
        [
            "SH-07",
            "Komunitas Open-Source Framework ML\n(Penyedia Library Scikit-Learn/ONNX)",
            "Ekosistem Komputasi Global Eksternal",
            "Rendah",
            "Rendah",
            "Kuadran IV:\nMonitor",
            "Memantau pembaruan keamanan pustaka, bug fixes, dan dokumentasi API versi terbaru secara pasif di repositori."
        ]
    ]
    create_table(doc, headers_reg, data_reg)

    # 2.2 Visualisasi Matriks Power/Interest Grid 2x2
    add_heading_3(doc, "b. Visualisasi Matriks Power/Interest Grid (2 × 2 Matrix)")
    add_body_p(doc,
        "Berikut adalah sintesis pemetaan posisi masing-masing pemangku kepentingan ke dalam matriks kuadran 2 × 2:")

    headers_grid = ["Dimensi Matriks", "Interest Rendah (Low Concern)", "Interest Tinggi (High Concern)"]
    data_grid = [
        [
            "Power Tinggi\n(High Authority)",
            "KUADRAN II: KEEP SATISFIED\n• SH-04: Ketua Program Studi TI\n• SH-05: Kepala Lab Komputasi Kampus\nStrategi: Laporan berkala tingkat tinggi, jaga kepatuhan SOP.",
            "KUADRAN I: MANAGE CLOSELY\n• SH-01: Dosen Pengampu (Dr. Ainul Yaqin)\n• SH-02: Project Manager / ML Lead\n• SH-03: Tim Pengembang Mahasiswa\nStrategi: Komunikasi intensif, kolaborasi aktif, rapat mingguan."
        ],
        [
            "Power Rendah\n(Low Authority)",
            "KUADRAN IV: MONITOR\n• SH-07: Komunitas Open-Source ML / Vendor\nStrategi: Pemantauan pasif melalui rilis informasi publik.",
            "KUADRAN III: KEEP INFORMED\n• SH-06: Praktisi Manajer Proyek Eksternal / User\nStrategi: Demonstrasi berkala, transparansi fitur, umpan balik."
        ]
    ]
    create_table(doc, headers_grid, data_grid)
