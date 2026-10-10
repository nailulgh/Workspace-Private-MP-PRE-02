# -*- coding: utf-8 -*-
"""
Section B Builder: Tugas Ringkasan Individu (Cost of Quality / COQ)
Pertemuan 8: Manajemen Kualitas Proyek
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

    add_heading_1(doc, "B. TUGAS RINGKASAN INDIVIDU: COST OF QUALITY (COQ)")

    # 1. Landasan Teori dan Filosofi COQ
    add_heading_2(doc, "1. Landasan Teori dan Filosofi Cost of Quality (COQ)")
    add_body_p(doc,
        "Cost of Quality (COQ) atau Biaya Kualitas adalah kerangka kerja finansial yang diperkenalkan oleh pakar kualitas "
        "Joseph M. Juran dan Philip B. Crosby, yang kemudian diadopsi secara resmi dalam standar PMBOK® Guide (PMI, 2017, Bab 8.1). "
        "COQ mendefinisikan total biaya moneter yang dikeluarkan oleh suatu organisasi untuk menegakkan mutu produk yang disepakati, "
        "ditambah dengan kerugian ekonomi yang timbul akibat kegagalan memenuhi standar kualitas tersebut. "
        "Filosofi modern menyatakan bahwa \"Quality is Free\" (Crosby, 1979)—artinya, berinvestasi pada kualitas sejak awal bukanlah pemborosan dana, "
        "melainkan instrumen penghematan biaya operasional paling masif karena mencegah pemborosan akibat cacat produk.")

    # 2. Taksonomi dan Empat Komponen Utama COQ
    add_heading_2(doc, "2. Taksonomi Empat Komponen Utama Cost of Quality")
    add_body_p(doc,
        "PMBOK Guide mengklasifikasikan COQ ke dalam dua pilar dikotomi utama: Biaya Kesesuaian (Cost of Conformance) "
        "dan Biaya Ketidaksesuaian (Cost of Nonconformance), yang terbagi ke dalam empat kuadran terukur:")

    add_heading_3(doc, "a. Biaya Kesesuaian (Cost of Conformance) – Investasi Proaktif")
    add_body_p(doc,
        "Biaya yang secara sadar dialokasikan selama proyek berjalan guna memastikan bahwa produk terhindar dari potensi cacat:")
    add_bullet_p(doc, "Prevention Costs (Biaya Pencegahan): Biaya desain dan tata kelola sistemik agar kesalahan tidak pernah terjadi sejak awal. Contoh: Workshop arsitektur software, pelatihan Clean Code bagi developer, penyusunan coding guidelines terstandarisasi, dan konfigurasi pipeline CI/CD otomatis.")
    add_bullet_p(doc, "Appraisal Costs (Biaya Penilaian / Inspeksi): Biaya pengujian, audit, dan pengukuran untuk mendeteksi apakah terjadi anomali sebelum deliverable diserahkan. Contoh: Pelaksanaan automated unit testing, static code analysis (SonarQube), peer code review antar developer, pengujian integrasi API, serta kalibrasi metrik validasi model machine learning.")

    add_heading_3(doc, "b. Biaya Ketidaksesuaian (Cost of Nonconformance) – Kerugian Reaktif")
    add_body_p(doc,
        "Biaya yang terpaksa dikeluarkan akibat terjadinya kegagalan kualitas atau pelanggaran spesifikasi:")
    add_bullet_p(doc, "Internal Failure Costs (Biaya Kegagalan Internal): Kerugian yang muncul ketika bug atau cacat ditemukan oleh tim internal sebelum produk dirilis ke pengguna/klien. Contoh: Waktu lembur untuk perbaikan bug (bug fixing), pengerjaan ulang (rework) modul yang gagal uji, pelatihan ulang model ML yang mengalami overfitting parah, dan komputasi ulang server GPU.")
    add_bullet_p(doc, "External Failure Costs (Biaya Kegagalan Eksternal): Bencana biaya yang terjadi saat cacat lolos ke lingkungan operasional pengguna akhir (production). Contoh: Downtime sistem yang melumpuhkan operasional klien, rilis patch darurat (hotfix), denda penalti keterlambatan kontrak (SLA penalty), hilangnya reputasi organisasi, hingga pembatalan proyek oleh sponsor.")

    # Tabel Komparasi COQ
    headers_coq = ["Kategori", "Komponen COQ", "Sifat Tindakan", "Contoh Proyek TI / Software", "Contoh Spesifik Riset PRE-02"]
    data_coq = [
        ["Cost of Conformance", "Prevention Cost", "Proaktif / Pencegahan", "Pelatihan arsitektur microservices & standar secure coding.", "Penyusunan protokol standardisasi ekstraksi 7 fitur proyek dan data hygiene."],
        ["Cost of Conformance", "Appraisal Cost", "Evaluasi / Pemeriksaan", "Audit kode otomatis, uji penetrasi keamanan, integration test.", "Pengujian metrik kalibrasi probabilitas (ECE, Brier Score, ROC-AUC) pada test fold."],
        ["Cost of Nonconformance", "Internal Failure", "Reaktif / Sebelum Rilis", "Refactoring kode spaghetti, penambalan memory leak saat QA.", "Retraining ulang model deep learning MLP akibat arsitektur awal tidak konvergen."],
        ["Cost of Nonconformance", "External Failure", "Krisis / Setelah Rilis", "Kompensasi insiden kebocoran data, pemulihan citra brand.", "Model memprediksi probabilitas keterlambatan salah total, memicu salah kelola portofolio bernilai miliaran."],
    ]
    create_table(doc, headers_coq, data_coq)

    # 3. Model Optimasi Total Cost of Quality
    add_heading_2(doc, "3. Model Optimasi dan Strategi Pengambilan Keputusan Manajer Proyek")
    add_body_p(doc,
        "Total Cost of Quality (TCOQ) dirumuskan secara matematis sebagai penjumlahan dari seluruh komponen: "
        "TCOQ = Prevention + Appraisal + Internal Failure + External Failure. "
        "Terdapat dinamika trade-off terbalik antara biaya kesesuaian dan biaya ketidaksesuaian:")
    add_bullet_p(doc, "Jika investasi pencegahan mendekati nol, maka biaya kegagalan (failure costs) akan melonjak tak terhingga menuju area kerugian kritis (critical loss zone).")
    add_bullet_p(doc, "Sebaliknya, jika organisasi berupaya mencapai kesempurnaan mutlak tanpa cacat (Zero Defect absolut) dengan pengujian tanpa henti, biaya kesesuaian dapat melonjak melebihi nilai ekonomis produk.")

    add_body_p(doc,
        "Strategi Optimalisasi bagi Manajer Proyek:")
    add_num_p(doc, "Menggeser Kurva ke Sisi Kiri (Front-Loading Quality): Mengalokasikan proporsi anggaran kualitas terbesar (60–70%) pada biaya pencegahan (Prevention) dan penilaian dini (Appraisal). Berdasarkan Aturan 1-10-100, menginvestasikan Rp 1 juta pada pencegahan menghemat potensi kerugian Rp 100 juta di lingkungan produksi.", 1)
    add_num_p(doc, "Menemukan Titik Optimum Ekonomi (Optimal Quality Level): Menentukan titik ekuilibrium di mana kurva Biaya Kesesuaian berpotongan dengan kurva Biaya Kegagalan, sehingga menghasilkan Total Biaya Kualitas yang paling minimal (minimum total cost of quality).", 2)
    add_num_p(doc, "Otomatisasi Pengujian (Automated Quality Pipeline): Memangkas biaya appraisal berulang dengan mengimplementasikan Continuous Integration / Continuous Deployment (CI/CD). Pengujian otomatis mengurangi biaya appraisal per iterasi mendekati nol seiring bertambahnya siklus pengembangan.", 3)
