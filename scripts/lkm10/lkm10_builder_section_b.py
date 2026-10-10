# -*- coding: utf-8 -*-
"""
Section B Builder: Tugas Latihan Individu
Pertemuan 10: Menghitung dan Menganalisis Saluran Komunikasi Proyek
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

    add_heading_1(doc, "B. TUGAS LATIHAN INDIVIDU: MENGHITUNG DAN MENGANALISIS SALURAN KOMUNIKASI PROYEK")

    add_body_p(doc,
        "Dalam manajemen proyek profesional berdasarkan standar PMBOK® Guide (PMI, 2017), saluran komunikasi potensial "
        "(potential communication channels) di antara para pemangku kepentingan dihitung menggunakan rumus kombinatorika graf lengkap (complete graph):")
    
    # Formula box / display paragraph
    p_box = doc.add_paragraph()
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_box.paragraph_format.space_before = Pt(4)
    p_box.paragraph_format.space_after = Pt(8)
    p_box.paragraph_format.line_spacing = 1.15
    r_box = p_box.add_run("C = n × (n - 1) / 2")
    r_box.font.name = "Times New Roman"
    r_box.font.size = Pt(13)
    r_box.font.bold = True

    add_body_p(doc,
        "Di mana:\n"
        "• C = Jumlah total saluran komunikasi potensial dua arah (potential communication channels).\n"
        "• n = Jumlah total pemangku kepentingan (stakeholders) dalam proyek, termasuk Manajer Proyek, anggota tim, sponsor, klien, dan pengguna akhir.")

    # =========================================================================
    # KASUS 1: SKENARIO 5 PEMANGKU KEPENTINGAN
    # =========================================================================
    add_heading_2(doc, "1. Perhitungan Saluran Komunikasi untuk Proyek dengan 5 Pemangku Kepentingan")
    add_body_p(doc,
        "Diketahui sebuah proyek rintisan memiliki jumlah pemangku kepentingan n = 5 orang. "
        "Langkah perhitungan matematis saluran komunikasi potensial adalah sebagai berikut:")
    
    add_bullet_p(doc, "Langkah 1: Identifikasi parameter jumlah pemangku kepentingan: n = 5.")
    add_bullet_p(doc, "Langkah 2: Substitusi nilai ke dalam rumus: C = 5 × (5 - 1) / 2")
    add_bullet_p(doc, "Langkah 3: Lakukan operasi perkalian pembilang: C = 5 × 4 / 2 = 20 / 2")
    add_bullet_p(doc, "Langkah 4: Hasil akhir: C = 10 saluran komunikasi.")
    
    add_body_p(doc,
        "Analisis Skenario 1: Pada proyek dengan 5 pemangku kepentingan (misalnya: 1 Manajer Proyek, 1 Lead Data Scientist, "
        "1 Machine Learning Engineer, 1 Backend Developer, dan 1 Product Owner), terdapat 10 kemungkinan jalur interaksi dua arah. "
        "Dengan 10 saluran, komunikasi masih berada pada tingkat kompleksitas rendah hingga moderat, di mana koordinasi tatap muka langsung "
        "dan rapat sinkronisasi harian masih sangat mudah dikelola tanpa risiko kelebihan beban informasi yang signifikan.")

    # =========================================================================
    # KASUS 2: SKENARIO 7 PEMANGKU KEPENTINGAN
    # =========================================================================
    add_heading_2(doc, "2. Perhitungan Saluran Komunikasi untuk Proyek dengan 7 Pemangku Kepentingan")
    add_body_p(doc,
        "Ketika tim proyek berkembang dan melibatkan pemangku kepentingan tambahan sehingga n = 7 orang. "
        "Langkah perhitungan matematis saluran komunikasi potensial adalah sebagai berikut:")
    
    add_bullet_p(doc, "Langkah 1: Identifikasi parameter jumlah pemangku kepentingan: n = 7.")
    add_bullet_p(doc, "Langkah 2: Substitusi nilai ke dalam rumus: C = 7 × (7 - 1) / 2")
    add_bullet_p(doc, "Langkah 3: Lakukan operasi perkalian pembilang: C = 7 × 6 / 2 = 42 / 2")
    add_bullet_p(doc, "Langkah 4: Hasil akhir: C = 21 saluran komunikasi.")
    
    add_body_p(doc,
        "Analisis Skenario 2: Pertambahan 2 orang anggota tim (dari 5 menjadi 7 orang) menyebabkan jumlah saluran komunikasi "
        "melonjak lebih dari dua kali lipat, dari 10 menjadi 21 saluran (peningkatan +110%). Pada titik ini, komunikasi spontan informal "
        "mulai menunjukkan keterbatasan, dan tim memerlukan aturan komunikasi dasar (ground rules) seperti rapat terjadwal dan saluran koordinasi terpusat.")

    # =========================================================================
    # KASUS 3: SKENARIO 10 PEMANGKU KEPENTINGAN DAN ANALISIS PENINGKATAN
    # =========================================================================
    add_heading_2(doc, "3. Perhitungan Saluran Komunikasi untuk Proyek dengan 10 Pemangku Kepentingan dan Analisis Peningkatannya")
    add_body_p(doc,
        "Jika skala proyek diperluas lebih lanjut dengan penambahan perwakilan sponsor eksternal, tim Quality Assurance, dan DevOps Engineer "
        "sehingga jumlah pemangku kepentingan mencapai n = 10 orang:")
    
    add_bullet_p(doc, "Langkah 1: Identifikasi parameter jumlah pemangku kepentingan: n = 10.")
    add_bullet_p(doc, "Langkah 2: Substitusi nilai ke dalam rumus: C = 10 × (10 - 1) / 2")
    add_bullet_p(doc, "Langkah 3: Lakukan operasi perkalian pembilang: C = 10 × 9 / 2 = 90 / 2")
    add_bullet_p(doc, "Langkah 4: Hasil akhir: C = 45 saluran komunikasi.")

    add_body_p(doc,
        "Analisis Komparasi dan Peningkatan Saluran (dari 7 menjadi 10 Pemangku Kepentingan):")
    add_bullet_p(doc, "Selisih Jumlah Pemangku Kepentingan (Δn): 10 - 7 = +3 pemangku kepentingan (peningkatan persentase: (3 / 7) × 100% = +42,86%).")
    add_bullet_p(doc, "Selisih Saluran Komunikasi Baru (ΔC): 45 - 21 = +24 saluran komunikasi baru.")
    add_bullet_p(doc, "Persentase Lonjakan Saluran Komunikasi: (24 / 21) × 100% = +114,29%.")

    add_body_p(doc,
        "Temuan Kritis: Penambahan pemangku kepentingan yang hanya sebesar 42,86% (3 orang) memicu lonjakan saluran komunikasi sebesar 114,29% (24 saluran baru). "
        "Rangkuman komparasi komprehensif disajikan pada Tabel 1 di bawah ini:")

    headers_table1 = ["Parameter Skenario", "Jumlah Stakeholder (n)", "Saluran Komunikasi (C)", "Pertambahan Saluran (ΔC)", "Persentase Lonjakan Saluran", "Tingkat Kompleksitas Koordinasi"]
    data_table1 = [
        ["Baseline Awal", "5 orang", "10 saluran", "–", "–", "Rendah – Komunikasi informal & tatap muka efektif."],
        ["Ekspansi Moderat", "7 orang", "21 saluran", "+11 saluran (dari n=5)", "+110,00%", "Moderat – Memerlukan jadwal rapat dan grup terstruktur."],
        ["Ekspansi Lanjutan", "10 orang", "45 saluran", "+24 saluran (dari n=7)", "+114,29%", "Tinggi – Memerlukan formalitas matriks komunikasi & klaster."]
    ]
    create_table(doc, headers_table1, data_table1)

    # =========================================================================
    # KASUS 4: IMPLIKASI PENINGKATAN JUMLAH STAKEHOLDER TERHADAP KOMPLEKSITAS
    # =========================================================================
    add_heading_2(doc, "4. Implikasi Peningkatan Jumlah Pemangku Kepentingan terhadap Kompleksitas Manajemen Komunikasi Proyek")
    add_body_p(doc,
        "Berdasarkan kalkulasi di atas, fenomena peningkatan jumlah pemangku kepentingan memberikan implikasi manajerial yang sangat mendalam "
        "terhadap kompleksitas pengelolaan proyek, diuraikan ke dalam empat dimensi analitis berikut:")

    add_num_p(doc, "Pertumbuhan Kompleksitas Non-Linier (Pertumbuhan Kuadratik O(n²)): Rumus saluran komunikasi berakar pada deret kombinatorika polinomial derajat dua. Penambahan satu anggota baru tidak hanya menambah satu jalur komunikasi, melainkan mengharuskan anggota baru tersebut membuka jalur hubungan komunikasi ke seluruh anggota tim yang telah ada sebelumnya. Hal ini berarti kompleksitas manajemen komunikasi tidak bertumbuh secara linier, melainkan secara eksponensial/kuadratik mendekati O(n²).", 1)
    add_num_p(doc, "Beban Koordinasi dan Hukum Brooks (Communication Overhead & Brooks's Law): Fred Brooks dalam karya klasiknya The Mythical Man-Month (1995) merumuskan bahwa \"menambah tenaga kerja pada proyek perangkat lunak yang terlambat justru akan membuatnya semakin terlambat\" (adding human resources to a late software project makes it later). Ketika pemangku kepentingan bertambah dari 7 menjadi 10 orang, waktu produktif kerja tim terdistraksi secara drastis untuk koordinasi, klarifikasi pesan, rapat berkepanjangan, dan sinkronisasi pemahaman. Biaya overhead komunikasi menggerus kapasitas eksekusi teknis.", 2)
    add_num_p(doc, "Entropi Informasi dan Risiko Distorsi Pesan (Information Entropy & Distortion): Dalam jaringan 45 saluran, risiko pesan mengalami efek \"telepon berbisik\" (Chinese whispers) meningkat tajam. Pesan yang berpindah melewati beberapa perantara rentan mengalami distorsi semantik, penyaringan informasi subjektif, atau salah tafsir spesifikasi teknis. Tanpa dokumentasi terpusat, konsistensi data arsitektur proyek akan runtuh.", 3)
    add_num_p(doc, "Potensi Eskalasi Friksi dan Konflik Interpersonal: Semakin banyak pihak yang terlibat, semakin beragam pula latar belakang, agenda politik, preferensi metodologi, dan ekspektasi yang dibawa. Diperlukan upaya diplomasi dan resolusi konflik yang jauh lebih intensif dari Manajer Proyek untuk menjaga konsensus tujuan tim.", 4)

    # =========================================================================
    # KASUS 5: STRATEGI MANAJER PROYEK MENGELOLA 10 PEMANGKU KEPENTINGAN
    # =========================================================================
    add_heading_2(doc, "5. Strategi Manajer Proyek untuk Mengelola Kompleksitas Komunikasi dengan 10 Pemangku Kepentingan")
    add_body_p(doc,
        "Untuk mencegah anarki komunikasi dan menjaga efisiensi eksekusi dalam tim proyek dengan 10 pemangku kepentingan (45 saluran komunikasi), "
        "seorang Manajer Proyek profesional wajib menerapkan lima strategi arsitektur komunikasi berikut:")

    add_num_p(doc, "Klasterisasi Komunikasi Berbasis Struktur Sub-Tim (Communication Clustering): Mengubah topologi jaringan komunikasi dari model \"mesh penuh\" (di mana setiap orang berbicara kepada setiap orang) menjadi model \"hierarkis terklaster\". Membagi 10 pemangku kepentingan ke dalam kelompok kerja fungsional:", 1)
    add_subbullet_p(doc, "Klaster Inti Teknis: Data Scientist, ML Engineer, Backend Developer, dan UI/UX Designer fokus pada koordinasi teknis internal.")
    add_subbullet_p(doc, "Klaster Tata Kelola & Bisnis: Sponsor, Product Owner, Manajer Proyek, dan Perwakilan Pengguna Akhir.")
    add_body_p(doc,
        "Arus komunikasi antar-klaster diatur melalui perwakilan resmi, sehingga mereduksi jumlah saluran aktif harian secara drastis.")

    add_num_p(doc, "Penunjukan Single Point of Contact (SPOC): Menetapkan juru bicara resmi untuk antarmuka eksternal. Manajer Proyek bertindak sebagai SPOC utama yang menjembatani tim pengembang teknis dengan para pemangku kepentingan bisnis dan dosen pembimbing. Dengan mekanisme ini, para pemangku kepentingan eksternal tidak diizinkan memberikan instruksi langsung kepada programmer individual, yang dapat mengacaukan prioritas sprint.", 2)

    add_num_p(doc, "Standardisasi Alur Informasi Menggunakan Matriks Komunikasi dan RACI: Menyusun dokumen formal Communications Management Plan yang memetakan secara tegas siapa yang memerlukan informasi apa, dalam format apa, dan frekuensi penyampaian yang ditentukan. Melalui pemetaan RACI, hanya pihak Responsible dan Accountable yang terlibat dalam eksekusi harian, sedangkan pemangku kepentingan lain cukup diposisikan sebagai Consulted atau Informed melalui laporan berkala.", 3)

    add_num_p(doc, "Transisi Menuju Model Pull Communication Terpusat (Single Source of Truth): Menghentikan ketergantungan pada rantai email massal dan obrolan grup instan yang tidak terstruktur. Seluruh artefak proyek—seperti arsitektur kode, dokumentasi API, hasil eksperimen model machine learning PRE-02, serta backlog pekerjaan—ditempatkan pada portal repositori sentral (misalnya GitHub Projects, Notion Workspace, atau Jira). Anggota tim dan sponsor dapat mengakses status proyek mutakhir secara mandiri tanpa membebani anggota lain.", 4)

    add_num_p(doc, "Protokol Rapat Terstruktur dan Budaya Komunikasi Asinkron (Asynchronous-First): Membatasi rapat tatap muka langsung hanya untuk agenda pengambilan keputusan strategis dan retrospektif mingguan dengan timeboxing ketat dan notula tertulis (minutes of meeting). Mengadopsi prinsip asinkron-pertama di mana pembaruan rutin disampaikan melalui laporan ringkas tertulis, sehingga anggota tim teknis memiliki waktu fokus mendalam (deep work) tanpa interupsi berulang.", 5)
