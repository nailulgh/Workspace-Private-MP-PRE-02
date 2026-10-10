# -*- coding: utf-8 -*-
"""
Section A Builder: Tugas Tertulis Individu
Pertemuan 7: Manajemen Biaya Proyek
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_a(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_heading_2 = helpers['add_heading_2']
    add_heading_3 = helpers['add_heading_3']
    add_body_p = helpers['add_body_p']
    add_num_p = helpers['add_num_p']
    add_bullet_p = helpers['add_bullet_p']
    add_subbullet_p = helpers['add_subbullet_p']
    create_table = helpers['create_table']

    add_heading_1(doc, "A. TUGAS TERTULIS INDIVIDU")

    # =========================================================================
    # SOAL 1
    # =========================================================================
    add_heading_2(doc, "1. Apa yang dimaksud dengan manajemen biaya proyek dan mengapa area pengetahuan ini penting dalam keberhasilan proyek?")
    add_body_p(doc,
        "Manajemen Biaya Proyek (Project Cost Management) mencakup serangkaian proses yang diperlukan "
        "untuk merencanakan, mengestimasi, menganggarkan, mendanai, mengatur, serta mengendalikan biaya "
        "agar proyek dapat diselesaikan dalam batas anggaran yang telah disetujui (PMBOK Guide 6th Ed). "
        "Area pengetahuan ini tidak hanya berfokus pada biaya tahap eksekusi, melainkan keseluruhan siklus "
        "hidup produk, termasuk biaya operasi dan pemeliharaan (life-cycle costing).")
    
    add_body_p(doc,
        "Manajemen biaya sangat krusial dalam keberhasilan proyek karena tiga alasan utama:")
    add_bullet_p(doc, "Mencegah Overbudget (Pembengkakan Biaya): Proyek TI seringkali mengalami cost overrun karena under-estimation beban kerja. Manajemen biaya memberikan instrumen pengendalian untuk memastikan pendanaan tidak melebihi kesepakatan.")
    add_bullet_p(doc, "Menjamin Return on Investment (ROI): Dengan mengelola pengeluaran dan memastikan cost benefit analysis tercapai, kelayakan finansial dari produk/layanan (seperti pada proyek PRE-02) dapat dipertahankan.")
    add_bullet_p(doc, "Menjadi Tolok Ukur Kinerja: Biaya adalah salah satu sisi dari segitiga manajemen proyek (Iron Triangle). Pengendalian biaya yang baik berfungsi sebagai metrik evaluasi kesehatan dan stabilitas proses pengerjaan proyek secara objektif.")

    # =========================================================================
    # SOAL 2
    # =========================================================================
    add_heading_2(doc, "2. Sebutkan dan jelaskan secara singkat empat proses dalam manajemen biaya proyek!")
    add_body_p(doc, "Menurut kerangka PMBOK 6th Edition, manajemen biaya proyek terdiri dari empat proses yang terstruktur:")
    
    add_num_p(doc, "Plan Cost Management (Merencanakan Manajemen Biaya)", 1)
    add_body_p(doc, 
        "Proses menetapkan kebijakan, prosedur, dan panduan untuk perencanaan, pengelolaan, "
        "pengeluaran, dan pengendalian biaya proyek. Hasilnya adalah Cost Management Plan.")
    
    add_num_p(doc, "Estimate Costs (Mengestimasi Biaya)", 2)
    add_body_p(doc, 
        "Proses pengembangan perkiraan nilai sumber daya moneter yang dibutuhkan untuk menyelesaikan "
        "seluruh pekerjaan proyek, seperti biaya server AWS, tarif per-jam programmer, dsb.")
    
    add_num_p(doc, "Determine Budget (Menentukan Anggaran)", 3)
    add_body_p(doc, 
        "Proses agregasi (penggabungan) dari seluruh estimasi biaya masing-masing aktivitas "
        "atau paket kerja (Work Package) untuk menetapkan Cost Baseline (tolok ukur biaya yang sah).")
    
    add_num_p(doc, "Control Costs (Mengendalikan Biaya)", 4)
    add_body_p(doc, 
        "Proses pemantauan status proyek untuk memutakhirkan anggaran serta mengelola "
        "perubahan pada baseline biaya. Pengendalian ini sering diimplementasikan dengan "
        "metode Earned Value Management (EVM).")

    # =========================================================================
    # SOAL 3
    # =========================================================================
    add_heading_2(doc, "3. Sebutkan dan jelaskan empat teknik estimasi biaya beserta kelebihan dan kekurangannya!")
    
    add_num_p(doc, "Analogous Estimating (Estimasi Analog)", 1)
    add_body_p(doc, "Menggunakan data historis dari proyek serupa sebelumnya (misalnya estimasi biaya PRE-01 digunakan untuk PRE-02).")
    add_bullet_p(doc, "Kelebihan: Cepat, murah, dan dapat digunakan saat informasi rinci masih minim di awal proyek.")
    add_bullet_p(doc, "Kekurangan: Tingkat akurasi paling rendah karena tiap proyek memiliki tingkat keunikan dan kompleksitas berbeda.")

    add_num_p(doc, "Parametric Estimating (Estimasi Parametrik)", 2)
    add_body_p(doc, "Menggunakan hubungan statistik antara data historis dan variabel lain (parameter), seperti biaya pembuatan 1 API endpoint = Rp 500.000, maka 10 API = Rp 5.000.000.")
    add_bullet_p(doc, "Kelebihan: Lebih akurat dari analogous, dapat diskalakan sesuai kuantitas atau ukuran parameter.")
    add_bullet_p(doc, "Kekurangan: Hanya efektif jika model parametrik yang mendasarinya valid dan data terukur dengan jelas.")

    add_num_p(doc, "Bottom-Up Estimating (Estimasi Bawah-Ke-Atas)", 3)
    add_body_p(doc, "Mengestimasi setiap komponen pekerjaan paling bawah (Work Package di WBS), lalu digabungkan (rollup) ke atas untuk mendapat total proyek.")
    add_bullet_p(doc, "Kelebihan: Akurasi sangat tinggi karena dirinci secara presisi pada setiap tugas spesifik.")
    add_bullet_p(doc, "Kekurangan: Sangat memakan waktu dan biaya besar, serta memerlukan WBS yang sudah final (rinci).")

    add_num_p(doc, "Three-Point Estimating (Estimasi Tiga Titik)", 4)
    add_body_p(doc, "Menggunakan tiga nilai estimasi: Optimistic (O), Most Likely (M), dan Pessimistic (P) dengan rumus PERT (O + 4M + P)/6.")
    add_bullet_p(doc, "Kelebihan: Memperhitungkan risiko dan tingkat ketidakpastian sehingga estimasi lebih realistis.")
    add_bullet_p(doc, "Kekurangan: Membutuhkan lebih banyak usaha untuk menggali tiga angka dari para pakar.")

    # =========================================================================
    # SOAL 4
    # =========================================================================
    add_heading_2(doc, "4. Apa perbedaan antara ROM (Rough Order of Magnitude) estimate dan Definitive estimate?")
    add_body_p(doc, 
        "Perbedaan utamanya terletak pada fase proyek saat estimasi dilakukan dan tingkat akurasi (rentang simpangan) "
        "yang dihasilkan:")
    add_bullet_p(doc, "Rough Order of Magnitude (ROM) Estimate: Dilakukan pada fase Inisiasi proyek (saat Project Charter dibuat). Akurasinya sangat kasar dengan rentang -25% hingga +75%. Tujuannya hanya untuk studi kelayakan atau persetujuan awal anggaran.")
    add_bullet_p(doc, "Definitive Estimate: Dilakukan di akhir fase Perencanaan, ketika WBS (Work Breakdown Structure) sudah lengkap dan vendor sudah jelas. Tingkat akurasinya jauh lebih presisi, dengan rentang -5% hingga +10%. Estimasi ini menjadi dasar penetapan Cost Baseline.")

    # =========================================================================
    # SOAL 5
    # =========================================================================
    add_heading_2(doc, "5. Jelaskan perbedaan antara contingency reserve dan management reserve! Kapan masing-masing digunakan?")
    add_body_p(doc, "Cadangan biaya (reserve) dibagi menjadi dua kategori berdasarkan jenis risikonya:")
    add_bullet_p(doc, "Contingency Reserve (Cadangan Kontingensi): Alokasi biaya yang disiapkan untuk mengantisipasi \"Known-Unknowns\" (risiko yang sudah teridentifikasi dalam Risk Register tetapi dampaknya belum pasti). Cadangan ini berada di DALAM Cost Baseline dan berada di bawah kendali penuh Manajer Proyek. Contoh: Cadangan biaya jika model ML PRE-02 memerlukan epoch training berulang akibat overfitting yang diprediksi.")
    add_bullet_p(doc, "Management Reserve (Cadangan Manajemen): Alokasi biaya untuk mengantisipasi \"Unknown-Unknowns\" (risiko force majeure atau kejadian yang tidak terprediksi sama sekali). Cadangan ini berada di LUAR Cost Baseline tetapi termasuk dalam total Project Budget. Penggunaannya harus dengan izin Sponsor Proyek atau manajemen senior. Contoh: Perubahan drastis regulasi privasi data atau pandemi mendadak.")

    # =========================================================================
    # SOAL 6
    # =========================================================================
    add_heading_2(doc, "6. Apa yang dimaksud dengan Earned Value Management (EVM) dan mengapa metodologi ini penting?")
    add_body_p(doc,
        "Earned Value Management (EVM) adalah metodologi pengukuran kinerja proyek yang mengintegrasikan "
        "ruang lingkup, jadwal, dan sumber daya biaya dalam satu kesatuan analisis objektif. EVM membandingkan "
        "nilai pekerjaan yang direncanakan dengan apa yang secara faktual diselesaikan (Earned) dan berapa banyak "
        "uang yang telah dikeluarkan (Actual).")
    add_body_p(doc,
        "Metodologi ini penting karena menghilangkan asumsi atau \"feeling\" subjektif tentang status proyek. "
        "Tanpa EVM, proyek yang menghabiskan 50% anggaran sering dianggap sudah 50% selesai, padahal "
        "kenyataan di lapangan (Earned Value) mungkin baru 30%. EVM mampu mendeteksi keterlambatan (schedule delay) "
        "dan pembengkakan biaya (cost overrun) sejak dini sehingga tindakan korektif dapat segera dieksekusi.")

    # =========================================================================
    # SOAL 7
    # =========================================================================
    add_heading_2(doc, "7. Sebutkan dan jelaskan tiga metrik dasar dalam EVM (PV, EV, AC) beserta cara menghitungnya!")
    
    add_bullet_p(doc, "Planned Value (PV): Nilai anggaran yang diotorisasi dan direncanakan untuk dikeluarkan hingga titik waktu tertentu. Rumus: PV = (Target % Progres Rencana) × Total Anggaran (BAC).")
    add_bullet_p(doc, "Earned Value (EV): Nilai aktual dari pekerjaan yang telah di-deliver atau diselesaikan secara fisik pada waktu tersebut. Rumus: EV = (Faktual % Progres Aktual) × Total Anggaran (BAC).")
    add_bullet_p(doc, "Actual Cost (AC): Total biaya rill atau kas kas keluar yang telah dihabiskan untuk menyelesaikan pekerjaan (EV) tersebut hingga tanggal pelaporan. Dihitung langsung berdasarkan tagihan kas/kuitansi proyek.")

    # =========================================================================
    # SOAL 8
    # =========================================================================
    add_heading_2(doc, "8. Jelaskan cara menghitung dan menginterpretasikan CV, SV, CPI, dan SPI!")
    
    add_bullet_p(doc, "Cost Variance (CV): Rumus: CV = EV - AC. Jika CV positif (> 0), proyek Under Budget (Hemat). Jika CV negatif (< 0), proyek Over Budget (Rugi/Boros).")
    add_bullet_p(doc, "Schedule Variance (SV): Rumus: SV = EV - PV. Jika SV positif (> 0), proyek Ahead of Schedule (Lebih cepat). Jika SV negatif (< 0), proyek Behind Schedule (Terlambat).")
    add_bullet_p(doc, "Cost Performance Index (CPI): Rumus: CPI = EV / AC. CPI adalah indikator efisiensi dana. CPI = 1.2 berarti setiap Rp 1 yang dikeluarkan menghasilkan Rp 1.2 (Sangat hemat). Jika CPI < 1.0 (misal 0.8), berarti proyek tidak efisien (boros).")
    add_bullet_p(doc, "Schedule Performance Index (SPI): Rumus: SPI = EV / PV. SPI adalah indikator efisiensi waktu. SPI = 1.1 berarti proyek berjalan 110% lebih cepat dari target. Jika SPI < 1.0, berarti progres eksekusi terlambat.")
