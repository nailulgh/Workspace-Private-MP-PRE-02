# -*- coding: utf-8 -*-
"""
Section B Builder: Tugas Individu (Studi Kasus Konflik Tim)
Pertemuan 9: Manajemen Sumber Daya Proyek
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

    add_heading_1(doc, "B. TUGAS INDIVIDU: ANALISIS DAN RESOLUSI STUDI KASUS KONFLIK TIM")

    # Narasi Kasus
    add_heading_2(doc, "1. Deskripsi Naratif Kasus Konflik Proyek")
    add_body_p(doc,
        "Studi Kasus: \"Dilema Integrasi Pipeline Model Machine Learning PRE-02 dan Arsitektur Backend API di Bawah Tekanan Tenggat Waktu\". "
        "Pada minggu ke-10 pengerjaan proyek sistem peringatan dini keterlambatan proyek, tim menghadapi kebuntuan (deadlock) "
        "antara Lead Data Scientist (Ahmad) dan Senior Backend Engineer (Budi):")
    add_bullet_p(doc, "Posisi Lead Data Scientist (Ahmad): Ahmad telah berhasil melatih model ensemble deep learning (MLP) dan Gradient Boosting berkategori berat dengan ukuran artefak biner 1,2 GB. Model ini menghasilkan metrik diskriminasi impresif dengan AUC-ROC 0,89 dan Brier Score 0,14. Namun, model tersebut membutuhkan waktu pemrosesan inferensi sekitar 1.800 milidetik (1,8 detik) per request dan konsumsi RAM yang sangat masif. Ahmad bersikeras bahwa model ini wajib dirilis apa adanya demi menjaga superioritas akurasi ilmiah.")
    add_bullet_p(doc, "Posisi Senior Backend Engineer (Budi): Budi menolak mentah-mentah untuk mengintegrasikan model tersebut ke dalam API gateway production. Mengacu pada arsitektur sistem, batas Service Level Agreement (SLA) response time API dashboard adalah maksimal 250 milidetik agar pengalaman pengguna tidak terganggu. Budi mengkhawatirkan jika model 1,2 GB dimuat ke server cloud, server akan mengalami Out-Of-Memory (OOM crash) saat diakses secara konkuren oleh puluhan manajer proyek. Budi menuntut Ahmad menyederhanakan model menjadi Logistic Regression biasa yang ringan (< 50 milidetik).")
    add_bullet_p(doc, "Eskalasi Ketegangan: Perdebatan substansi teknis mulai merembet menjadi serangan personal saat rapat evaluasi. Budi menuduh Ahmad \"hanya mengejar prestasi akademis di atas kertas tanpa mempedulikan realitas infrastruktur\", sementara Ahmad membalas dengan menuduh Budi \"tidak memahami esensi kecerdasan buatan dan malas mengoptimasi arsitektur cloud server\". Akibatnya, komunikasi kedua pihak terputus dan proses integrasi sistem terhenti selama 5 hari kerja.")

    # Pertanyaan 1: Identifikasi Jenis Konflik
    add_heading_2(doc, "2. Identifikasi dan Dekomposisi Jenis Konflik yang Terjadi")
    add_body_p(doc,
        "Berdasarkan tipologi konflik dari Jehn (1995) dan riset University of Texas at El Paso, kasus di atas mencerminkan "
        "fenomena 'Konflik Berlapis' (Multi-layered Escalated Conflict) yang bermula dari substansi teknis lalu bermutasi:")
    add_num_p(doc, "Konflik Utama – Task Conflict (Konflik Tugas): Perselisihan fundamental terjadi pada konten teknis deliverables, yaitu benturan antara target performa akurasi statistik machine learning (AUC-ROC & Brier Score) melawan target performa rekayasa sistem (latensi respons API dan efisiensi konsumsi memori server). Ini merupakan konflik substantif yang wajar dalam rekayasa perangkat lunak cerdas.", 1)
    add_num_p(doc, "Konflik Sekunder – Process Conflict (Konflik Proses): Terjadi ketidakjelasan mengenai 'siapa yang memiliki wewenang final' untuk menetapkan ambang batas Definition of Done (DoD) rilis sistem, serta ketiadaan protokol pengujian beban (load testing) bersama sejak fase awal pembuatan model.", 2)
    add_num_p(doc, "Eskalasi Berbahaya – Relationship Conflict (Konflik Hubungan Interpersonal): Ketika argumen beralih dari mendiskusikan metrik teknis menjadi saling menyerang kompetensi dan motif profesional (menuduh 'akademisi naif' vs 'engineer malas'), konflik telah bergeser ke ranah personal. Jika tidak segera dihentikan oleh Manajer Proyek, konflik relasional ini akan merusak psikologis tim secara permanen.", 3)

    # Pertanyaan 2: Pemilihan Strategi Resolusi
    add_heading_2(doc, "3. Penentuan Strategi Resolusi Konflik yang Paling Tepat")
    add_body_p(doc,
        "Strategi yang PALING TEPAT dan WAJIB diterapkan oleh Manajer Proyek adalah: Collaborating / Problem Solving (Pendekatan Kolaboratif Berorientasi Solusi Win-Win).")
    add_body_p(doc, "Alasan Pemilihan Strategi Kolaboratif:")
    add_bullet_p(doc, "Kepentingan Kedua Belah Pihak Sama-Sama Vital: Proyek PRE-02 tidak boleh mengorbankan akurasi prediksi karena sistem peringatan dini yang tidak akurat akan menyesatkan manajer proyek. Namun, proyek juga tidak boleh merilis sistem yang lambat dan rentan tumbang (crash). Kedua parameter mutu tersebut mutlak diperlukan.")
    add_bullet_p(doc, "Menghindari Dampak Negatif Strategi Lain: Forcing (memaksakan salah satu pihak) akan menciptakan kebencian dan demotivasi bagi pihak yang kalah. Avoiding (menghindar) akan menggagalkan deadline rilis. Compromising murni (mengorbankan separuh akurasi dan separuh latensi secara serampangan) berisiko menghasilkan produk yang setengah matang di kedua aspek.")
    add_bullet_p(doc, "Peluang Inovasi Teknologi Bersama: Pendekatan kolaboratif memaksa kedua disiplin ilmu (Data Science dan Software Engineering) untuk mencari terobosan teknis yang sebelumnya tidak terpikirkan jika mereka bekerja terisolasi.")

    # Pertanyaan 3: Rekomendasi Langkah Konkret Pendekatan Kolaboratif
    add_heading_2(doc, "4. Rekomendasi Langkah-Langkah Konkret Penyelesaian Kolaboratif")
    add_body_p(doc,
        "Sebagai Manajer Proyek, saya akan memfasilitasi rekonsiliasi teknis melalui empat tahapan terstruktur:")
    
    add_num_p(doc, "Langkah 1: Fasilitasi Sesi Mediasi Tertutup dan De-eskalasi Emosi (Cooling-off & Reframing)", 1)
    add_body_p(doc, 
        "Mengumpulkan Ahmad dan Budi dalam ruang diskusi tertutup. Menegaskan aturan dasar bahwa serangan personal "
        "tidak ditoleransi dan mengarahkan kembali fokus pada tujuan bersama (superordinate goal): 'Menghasilkan sistem PRE-02 yang akurat sekaligus responsif bagi pengguna'.")

    add_num_p(doc, "Langkah 2: Eksplorasi Solusi Rekayasa Kompromistis Melalui Model Quantization & Format ONNX", 2)
    add_body_p(doc,
        "Mengajak kedua ahli merumuskan solusi rekayasa modern tanpa saling meniadakan:")
    add_subbullet_p(doc, "Optimasi Model (Data Science): Ahmad melakukan konversi model ke format standar terbuka ONNX Runtime serta menerapkan teknik Post-Training Quantization (mengubah bobot float32 ke int8) dan Pruning bobot tidak signifikan. Langkah ini terbukti mampu memangkas ukuran model dari 1,2 GB menjadi hanya 120 MB tanpa mengorbankan akurasi (degradasi AUC-ROC kurang dari 0,005).")
    add_subbullet_p(doc, "Optimasi Arsitektur Backend (Software Engineering): Budi membangun caching layer berbasis Redis untuk menyimpan hasil inferensi dari profil proyek yang sering diakses, serta memisahkan inferensi model ke dalam worker pool asynchronous (Celery/FastAPI Background Tasks), sehingga response time dashboard turun menjadi 80 milidetik.")

    add_num_p(doc, "Langkah 3: Pengujian Bersama pada Lingkungan Staging (Joint Validation)", 3)
    add_body_p(doc,
        "Ahmad dan Budi melakukan stress testing bersama di server staging. Hasil empiris diverifikasi secara objektif: latensi API tercapai 85 ms (< target 250 ms) dan nilai AUC-ROC tetap unggul di angka 0,885 (> target baseline 0,80). Keduanya meraih kemenangan teknis (Win-Win).")

    add_num_p(doc, "Langkah 4: Rekonsiliasi Hubungan dan Apresiasi Publik", 4)
    add_body_p(doc,
        "Pada sesi sprint review tim, Manajer Proyek secara terbuka mengapresiasi kolaborasi Ahmad dan Budi yang berhasil melahirkan terobosan pipeline MLOps yang sangat efisien bagi keberlanjutan produk.")

    # Pertanyaan 4: Pencegahan di Masa Depan
    add_heading_2(doc, "5. Langkah Preventif Manajer Proyek untuk Mencegah Konflik Serupa di Masa Depan")
    add_body_p(doc, "Guna mencegah friksi integrasi serupa pada fase proyek berikutnya, Manajer Proyek wajib menetapkan empat instrumen tata kelola:")
    add_num_p(doc, "Penerapan Kerangka Kerja MLOps (Cross-Functional Collaboration) Sejak Hari Pertama: Mengintegrasikan tim Data Science dan tim Backend dalam satu siklus sprint yang sama, bukan model estafet terpisah. Data Scientist wajib memahami batasan deployment, dan Software Engineer wajib memahami alur training model.", 1)
    add_num_p(doc, "Menyusun Definition of Done (DoD) Multidimensi yang Jelas: Menetapkan kriteria penerimaan resmi pada WBS Dictionary bahwa deliverables model ML dinyatakan 'selesai' bukan hanya jika metrik AUC-ROC ≥ 0,80, melainkan juga jika ukuran artefak model ≤ 200 MB dan latensi inferensi ≤ 200 ms.", 2)
    add_num_p(doc, "Penyusunan RACI Chart yang Tegas pada Fase Integrasi: Menetapkan peran Accountable (A) yang jelas untuk setiap gerbang rilis (quality gate), sehingga tidak terjadi perebutan wewenang atau perdebatan kusir saat deployment.", 3)
    add_num_p(doc, "Menyepakati Team Charter dan Protokol Komunikasi: Memformalkan aturan main dalam tim mengenai etika pemberian umpan balik saat code review dan mekanisme eskalasi perbedaan teknis sebelum berubah menjadi serangan personal.", 4)
