# -*- coding: utf-8 -*-
"""
Section C Builder: Tugas Praktik Individu (Fishbone Diagram & Pareto Chart)
Pertemuan 8: Manajemen Kualitas Proyek
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

    add_heading_1(doc, "C. TUGAS PRAKTIK INDIVIDU: PENERAPAN ALAT KUALITAS DASAR")

    # =========================================================================
    # PRAKTIK 1: FISHBONE DIAGRAM
    # =========================================================================
    add_heading_2(doc, "1. Praktik 1: Cause-and-Effect Diagram (Fishbone Diagram) Kasus Bug Pengujian Aplikasi")
    add_body_p(doc,
        "Studi Kasus: Sebuah proyek pengembangan perangkat lunak mengalami keterlambatan pengiriman (delivery delay) "
        "yang disebabkan oleh melonjaknya temuan cacat/bug kritis pada tahap pengujian akhir (QA testing). "
        "Untuk mengidentifikasi akar penyebab sistemik di balik fenomena ini, dilakukan analisis sebab-akibat menggunakan "
        "kerangka kerja 5M (Man, Machine, Method, Material, Measurement) yang disesuaikan dengan konteks rekayasa perangkat lunak modern:")

    add_heading_3(doc, "Dekomposisi Akar Penyebab (Root Cause Analysis - 5M Framework):")
    
    add_num_p(doc, "Man (Sumber Daya Manusia / Tim Pengembang):", 1)
    add_subbullet_p(doc, "Kurangnya pemahaman developer terhadap spesifikasi kebutuhan fungsional (ambiguitas user story dari sistem analis).")
    add_subbullet_p(doc, "Tingkat kelelahan kerja ekstrem (burnout / over-utilization) akibat lembur terus-menerus, memicu tingginya human error.")
    add_subbullet_p(doc, "Ketiadaan pelatihan formal mengenai penulisan Unit Testing otomatis dan praktik Secure Coding.")

    add_num_p(doc, "Machine / Technology (Infrastruktur, Perangkat Keras, & Tools Pengembangan):", 2)
    add_subbullet_p(doc, "Ketidaksesuaian konfigurasi (environment drift) antara lingkungan pengembangan lokal (localhost), staging, dan testing.")
    add_subbullet_p(doc, "Pipeline integrasi berkelanjutan (CI/CD) belum mengintegrasikan alat Static Application Security Testing (SAST) otomatis.")
    add_subbullet_p(doc, "Spesifikasi server staging terbatas sehingga gagal mendeteksi memory leak dan konkurensi di bawah beban tinggi.")

    add_num_p(doc, "Method (Metodologi Rekayasa & Standar Prosedur Operasional):", 3)
    add_subbullet_p(doc, "Prosedur Code Review dilakukan secara terburu-buru (hanya formalitas persetujuan Pull Request tanpa verifikasi mendalam).")
    add_subbullet_p(doc, "Tidak adanya kriteria Definition of Done (DoD) yang disepakati bersama sebelum tugas dinyatakan selesai.")
    add_subbullet_p(doc, "Pendekatan pengujian bergaya \"Big-Bang Testing\" di akhir fase rilis alih-alih pengujian bertahap sejak awal sprint.")

    add_num_p(doc, "Material / Data (Dataset Pengujian & Dependensi Perangkat Lunak):", 4)
    add_subbullet_p(doc, "Dataset pengujian dummy yang digunakan developer terlalu bersih dan homogen, tidak merepresentasikan variasi data riil kotor.")
    add_subbullet_p(doc, "Penggunaan pustaka (libraries) dan modul pihak ketiga usang yang memiliki kerentanan serta cacat bawaan.")
    add_subbullet_p(doc, "Skema database staging tidak sinkron dengan migrasi struktur data aplikasi terbaru.")

    add_num_p(doc, "Measurement (Metrik Kualitas & Kriteria Pengukuran):", 5)
    add_subbullet_p(doc, "Target code coverage unit test terlalu rendah (< 40%) namun deliverable tetap dipaksakan lolos ke tahap QA.")
    add_subbullet_p(doc, "Klasifikasi tingkat keparahan bug (severity & priority) tidak terdefinisi jelas, menimbulkan perdebatan saat triage.")
    add_subbullet_p(doc, "Ketiadaan metrik pemantauan Defect Density harian untuk mendeteksi tren lonjakan cacat secara dini.")

    # Tabel Ringkasan Fishbone
    headers_fishbone = ["Dimensi 5M", "Akar Penyebab Utama (Root Cause)", "Rekomendasi Tindakan Korektif & Preventif"]
    data_fishbone = [
        ["Man", "Developer kelelahan & minim skill testing.", "Melakukan resource leveling beban kerja dan pelatihan unit test."],
        ["Machine", "Environment drift antara lokal & staging.", "Standardisasi kontainerisasi menggunakan Docker dan perbaikan pipeline CI."],
        ["Method", "Code review longgar & testing terlambat.", "Menegakkan aturan wajib minimal 2 reviewer approval dan DoD ketat."],
        ["Material", "Data uji tidak realistis & library usang.", "Penyediaan mock data produksi yang disanitasi & audit dependensi."],
        ["Measurement", "Metrik code coverage rendah (< 40%).", "Menetapkan automated quality gate: build gagal jika coverage < 80%."],
    ]
    create_table(doc, headers_fishbone, data_fishbone)

    # =========================================================================
    # PRAKTIK 2: PARETO CHART
    # =========================================================================
    add_heading_2(doc, "2. Praktik 2: Pareto Chart dan Analisis Prioritas Kualitas 80/20")
    add_body_p(doc,
        "Diberikan data temuan cacat produk dari sampel pengujian sebanyak 100 unit sebagai berikut: "
        "Cacat A (45 unit), Cacat B (30 unit), Cacat C (15 unit), Cacat D (8 unit), dan Cacat E (2 unit). "
        "Berikut adalah tabel perhitungan analisis Pareto yang menyajikan frekuensi absolut, proporsi persentase individual, "
        "serta persentase kumulatif yang telah diurutkan dari frekuensi terbesar:")

    headers_pareto = ["Kode Cacat", "Kategori Jenis Cacat", "Frekuensi (Unit)", "Persentase Individual (%)", "Persentase Kumulatif (%)", "Klasifikasi Pareto"]
    data_pareto = [
        ["A", "Cacat Logika / Fungsional Utama", "45", "45,0%", "45,0%", "Vital Few (Prioritas 1)"],
        ["B", "Cacat Validasi Input & Tampilan (UI/UX)", "30", "30,0%", "75,0%", "Vital Few (Prioritas 2)"],
        ["C", "Cacat Kompatibilitas Browser/OS", "15", "15,0%", "90,0%", "Useful Many (Sekunder)"],
        ["D", "Cacat Performa / Respons Lambat", "8", "8,0%", "98,0%", "Trivial Many (Tersier)"],
        ["E", "Cacat Penulisan Teks / Tipografi", "2", "2,0%", "100,0%", "Trivial Many (Tersier)"],
        ["TOTAL", "Keseluruhan Sampel Cacat", "100", "100,0%", "-", "-"],
    ]
    create_table(doc, headers_pareto, data_pareto)

    add_heading_3(doc, "Interpretasi dan Analisis Prinsip Pareto (Prinsip 80/20):")
    add_body_p(doc,
        "Prinsip Pareto (80/20 Rule) menyatakan bahwa sekitar 80% dari dampak masalah disebabkan oleh 20% penyebab utama. "
        "Berdasarkan tabel distribusi di atas, diperoleh temuan analitis strategis:")
    add_bullet_p(doc, "Identifikasi \"Vital Few\" (Penyebab Krusial): Dua kategori cacat pertama, yaitu Cacat A (45%) dan Cacat B (30%), secara akumulatif menyumbang 75,0% (mendekati 80%) dari keseluruhan populasi cacat produk.")
    add_bullet_p(doc, "Identifikasi \"Trivial Many\" (Penyebab Sepele): Tiga kategori lainnya, yaitu Cacat C (15%), Cacat D (8%), dan Cacat E (2%), jika digabungkan hanya menyumbang 25,0% dari total masalah.")
    
    add_body_p(doc,
        "Keputusan Manajerial Proyek:")
    add_num_p(doc, "Fokus Alokasi Sumber Daya: Tim pengembang tidak boleh membagi waktu secara rata ke semua jenis cacat. Sebanyak 80% alokasi waktu perbaikan bug dan jam kerja tim QA harus dipusatkan untuk menuntaskan Cacat A dan Cacat B terlebih dahulu.", 1)
    add_num_p(doc, "Efektivitas Peningkatan Kualitas: Dengan berhasil menuntaskan Cacat A dan B, 75% permasalahan kualitas proyek akan langsung tereliminasi dalam satu siklus perbaikan, yang akan memulihkan jadwal proyek secara drastis tanpa menghabiskan anggaran.", 2)
    add_num_p(doc, "Penanganan Cacat Tersier: Cacat D dan E dapat ditangguhkan ke siklus pemeliharaan minor berikutnya (post-launch maintenance) karena tidak menghambat fungsi inti sistem.", 3)
