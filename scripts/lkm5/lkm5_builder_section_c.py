# -*- coding: utf-8 -*-
"""
Section C Builder: Tugas Kelompok (Daftar Aktivitas & Estimasi Durasi Proyek PRE-02)
Pertemuan 5: Manajemen Jadwal Proyek (Bagian I)
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_c(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_heading_2 = helpers['add_heading_2']
    add_heading_3 = helpers['add_heading_3']
    add_body_p = helpers['add_body_p']
    add_num_p = helpers['add_num_p']
    add_bullet_p = helpers['add_bullet_p']
    add_subbullet_p = helpers['add_subbullet_p']
    create_table = helpers['create_table']

    add_heading_1(doc, "C. TUGAS KELOMPOK: DAFTAR AKTIVITAS DAN ESTIMASI DURASI PROYEK PRE-02")

    add_body_p(doc,
        "Sebagai bentuk implementasi kontekstual dari proses Define Activities, Sequence Activities, dan Estimate Activity Durations, "
        "bagian ini menyajikan dekomposisi paket kerja (work packages) dari WBS proyek kelompok berkode PRE-02:")
    add_bullet_p(doc, "Nama Proyek Kelompok:", "Sistem Prediksi Probabilitas Keterlambatan Proyek Berbasis Machine Learning sebagai Early Warning System Manajemen Proyek (Kode: PRE-02).")
    add_bullet_p(doc, "Objek Studi Kasus:", "Portofolio Multi-Proyek Pengembangan 8 Modul Super ERP Farm Nation Enterprise (FNE) 2026.")
    add_bullet_p(doc, "Dasar Dekomposisi:", "WBS Level 3 & Level 4 yang telah diformulasikan pada LKM 4 (Manajemen Ruang Lingkup Proyek).")

    # =========================================================================
    # TABEL DAFTAR AKTIVITAS (ACTIVITY LIST)
    # =========================================================================
    add_heading_2(doc, "1. Matriks Daftar Aktivitas (Activity List), Ketergantungan, dan Estimasi Durasi Proyek PRE-02")
    
    add_body_p(doc,
        "Berikut adalah daftar 16 aktivitas kerja spesifik proyek PRE-02 yang memuat kode aktivitas, dekomposisi WBS induk, deskripsi "
        "aksi teknis, predecessor dan tipe ketergantungan (seluruhnya menggunakan hubungan Finish-to-Start / FS), teknik estimasi durasi "
        "yang diterapkan, estimasi durasi dalam satuan hari kerja kalender, serta penanggung jawab (Person In Charge / PIC):")

    table_data_act = [
        ["1.1.1", "ACT-01", "Perumusan Spesifikasi 7 Fitur Prediktor", "Mendefinisikan definisi operasional 7 fitur kondisi proyek (Progress, Deadline, Backlog, SDM, Risk, CR, Dependency) dan target probabilitas.", "-", "Analogous", "3", "Lead Author"],
        ["1.1.2", "ACT-02", "Penyusunan Project Charter & Schedule Plan", "Menyusun dokumen tata kelola integrasi proyek, baseline waktu, dan rencana manajemen jadwal perkuliahan.", "ACT-01 (FS)", "Analogous", "2", "Lead Author"],
        ["2.1.1", "ACT-03", "Studi Literatur Model Prediksi Proyek", "Melakukan telaah sistematis atas 10+ jurnal internasional mengenai Machine Learning untuk keterlambatan proyek.", "ACT-01 (FS)", "Three-Point (PERT)", "5", "Lead Author"],
        ["2.1.2", "ACT-04", "Penyusunan Matriks Literatur & Research Gap", "Memetakan kelemahan klasifikasi biner dan merumuskan celah riset probabilitas numerik kontinu terkalibrasi.", "ACT-03 (FS)", "Three-Point (PERT)", "3", "Lead Author"],
        ["3.1.1", "ACT-05", "Ekstraksi Data Mentah dari Dokumen PMP ERP", "Mengekstraksi riwayat metrik dari 8 dokumen PMP & SRS modul Super ERP Farm Nation Enterprise ke format CSV.", "ACT-02 (FS)", "Bottom-Up", "4", "Data Engineer"],
        ["3.1.2", "ACT-06", "Pembersihan Data & Imputasi Missing Values", "Menjalankan pipeline pembersihan data, penanganan nilai anomali/outlier, dan imputasi nilai kosong pada dataset mentah.", "ACT-05 (FS)", "Three-Point (PERT)", "3", "Data Engineer"],
        ["3.1.3", "ACT-07", "Feature Engineering & Normalisasi Fitur", "Melakukan penskalaan fitur (Min-Max Scaling), pembobotan Dependency Score, dan pembentukan label probabilitas target.", "ACT-06 (FS)", "Three-Point (PERT)", "3", "Data Engineer"],
        ["3.1.4", "ACT-08", "Pembagian Dataset (Stratified Split)", "Membagi dataset bersih menjadi 80% Training Set dan 20% Testing Set dengan distribusi kelas terstratifikasi.", "ACT-07 (FS)", "Parametric", "1", "Data Engineer"],
        ["4.1.1", "ACT-09", "Pengembangan Baseline Logistic Regression", "Mengembangkan arsitektur model regresi logistik baseline dengan output fungsi sigmoid untuk estimasi probabilitas dasar.", "ACT-08 (FS)", "Three-Point (PERT)", "3", "ML Engineer"],
        ["4.1.2", "ACT-10", "Pengembangan Model Random Forest", "Mengembangkan model ensemble Random Forest dengan predict_proba dan ekstraksi grafik Feature Importance.", "ACT-08 (FS)", "Three-Point (PERT)", "4", "ML Engineer"],
        ["4.1.3", "ACT-11", "Pengembangan Model Gradient Boosting", "Mengembangkan model Gradient Boosting / XGBoost dengan minimisasi log-loss deviance untuk menangani hubungan non-linier.", "ACT-08 (FS)", "Three-Point (PERT)", "4", "ML Engineer"],
        ["4.1.4", "ACT-12", "Pengembangan Model Neural Network (MLP)", "Membangun arsitektur Multi-Layer Perceptron (16-8 hidden nodes) dengan aktivasi ReLU dan output sigmoid.", "ACT-08 (FS)", "Three-Point (PERT)", "5", "ML Engineer"],
        ["4.2.1", "ACT-13", "Implementasi Kalibrasi Probabilitas", "Menerapkan metode kalibrasi Platt Scaling dan Isotonic Regression pada output probabilitas seluruh model ML.", "ACT-09, ACT-10, ACT-11, ACT-12 (FS)", "Bottom-Up", "4", "ML Engineer"],
        ["5.1.1", "ACT-14", "Evaluasi Metrik Probabilitas & Brier Score", "Menghitung nilai evaluasi Brier Score (<0.18), Log-Loss, ROC-AUC (>=0.80), dan Expected Calibration Error (ECE).", "ACT-13 (FS)", "Parametric", "3", "ML Engineer"],
        ["5.1.2", "ACT-15", "Analisis Ambang Batas Peringatan Dini (EWS)", "Menentukan threshold optimal (Youden J Index) untuk memicu sinyal bahaya keterlambatan pada level probabilitas >=0.65.", "ACT-14 (FS)", "Three-Point (PERT)", "2", "Lead Author"],
        ["6.1.1", "ACT-16", "Penyusunan Paper Lengkap & Slide Presentasi", "Mengintegrasikan naskah ilmiah format IMRAD (Bab 1–5), tabel matriks, plot kurva kalibrasi, serta slide presentasi progres.", "ACT-04, ACT-15 (FS)", "Bottom-Up", "5", "All Team"]
    ]

    create_table(doc, [1.4, 1.4, 3.2, 4.3, 2.2, 2.0, 1.2, 1.8],
                 ["WBS ID", "Kode", "Nama Aktivitas", "Deskripsi Pekerjaan", "Predecessor", "Teknik Estimasi", "Durasi (Hr)", "PIC"],
                 table_data_act,
                 align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT,
                             WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER,
                             WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])

    # =========================================================================
    # ELABORASI LOGIKA JADWAL PRE-02
    # =========================================================================
    add_heading_2(doc, "2. Analisis Logika Pengurutan Ketergantungan dan Jalur Kritis Proyek PRE-02")
    
    add_body_p(doc,
        "Penyusunan daftar aktivitas dan ketergantungan di atas didasarkan pada prinsip-prinsip rekayasa perangkat lunak dan metodologi "
        "data science yang ketat:")

    add_num_p(doc, "1.", "Alur Ketergantungan Pipeline Machine Learning (Mandatory Dependencies):",
        "Dalam alur kerja machine learning, pemrosesan data bersifat sekuensial mutlak (Hard Logic). Pembersihan data (ACT-06) tidak dapat "
        "dimulai sebelum data mentah diekstraksi (ACT-05). Feature engineering (ACT-07) mutlak memerlukan data yang telah bersih dari "
        "missing values. Lebih lanjut, pelatihan keempat model machine learning (ACT-09 s.d. ACT-12) baru dapat dieksekusi secara serentak "
        "setelah proses pembagian dataset (ACT-08) selesai secara tuntas.")

    add_num_p(doc, "2.", "Konvergensi Kalibrasi Probabilitas (Merge Activity):",
        "Aktivitas ACT-13 (Kalibrasi Probabilitas) merupakan simpul penggabungan kritis yang menuntut penyelesaian penuh dari keempat model "
        "algoritma (Logistic Regression, Random Forest, Gradient Boosting, dan MLP). Langkah ini esensial karena kalibrasi probabilitas "
        "(Platt Scaling dan Isotonic Regression) memerlukan perbandingan matriks probabilitas tidak terkalibrasi dari seluruh arsitektur model "
        "guna memilih algoritma dengan Expected Calibration Error (ECE) terendah.")

    add_num_p(doc, "3.", "Identifikasi Lintasan Jalur Kritis Internal PRE-02:",
        "Berdasarkan rantai ketergantungan logis di atas, lintasan terpanjang yang mengendalikan total durasi penyelesaian riset PRE-02 adalah:\n"
        "ACT-01 (3 hr) → ACT-02 (2 hr) → ACT-05 (4 hr) → ACT-06 (3 hr) → ACT-07 (3 hr) → ACT-08 (1 hr) → ACT-12 (5 hr) → ACT-13 (4 hr) "
        "→ ACT-14 (3 hr) → ACT-15 (2 hr) → ACT-16 (5 hr).\n"
        "Total Durasi Jalur Kritis Proyek PRE-02 adalah: 35 Hari Kalender.\n"
        "Sementara itu, aktivitas cabang penelaahan literatur (ACT-03 dan ACT-04) memiliki total durasi 8 hari dan berjalan secara paralel "
        "setelah ACT-01, sehingga memiliki kelonggaran waktu (Total Float) yang melimpah (TF = 22 hari) sebelum menyatu pada ACT-16.")

    add_num_p(doc, "4.", "Rasionalitas Pemilihan Teknik Estimasi:",
        "Teknik Three-Point Estimating (PERT) mendominasi aktivitas pemodelan algoritma dan feature engineering (ACT-06, ACT-07, ACT-09 s.d. "
        "ACT-12). Hal ini dikarenakan proses pelatihan kecerdasan buatan sarat dengan ketidakpastian eksperimental—seperti potensi terjadinya "
        "overfitting, konvergensi gradient descent yang lambat, serta kebutuhan tuning hyperparameter. Sebaliknya, teknik Parametric "
        "digunakan pada tugas deterministik seperti pembagian dataset dan evaluasi metrik (ACT-08 dan ACT-14), sedangkan teknik Bottom-Up "
        "diterapkan pada aktivitas integrasi deliverable akhir (ACT-16).")
