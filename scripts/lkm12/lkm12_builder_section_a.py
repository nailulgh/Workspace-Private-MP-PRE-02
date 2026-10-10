# -*- coding: utf-8 -*-
"""
Section A Builder: Tugas Tertulis Individu
Pertemuan 12: Manajemen Risiko Proyek (Bagian II)
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
    add_heading_2(doc, "1. Apa yang dimaksud dengan analisis risiko kuantitatif dan apa tujuan utama dari proses ini?")
    add_body_p(doc,
        "Analisis Risiko Kuantitatif (Perform Quantitative Risk Analysis) adalah proses manajemen proyek yang menganalisis secara numerik "
        "efek gabungan dari risiko-risiko individu proyek yang telah diprioritaskan beserta sumber ketidakpastian lainnya terhadap "
        "sasaran proyek secara keseluruhan (PMBOK® Guide 6th Edition, PMI, 2017, hal. 428–436). Berbeda dengan analisis kualitatif yang "
        "menghasilkan skor deskriptif relatif (seperti status Tinggi/Sedang/Rendah), analisis kuantitatif menggunakan pemodelan matematika, "
        "teori probabilitas statistik, dan simulasi numerik untuk mengonversi ketidakpastian menjadi estimasi moneter (biaya) atau durasi waktu yang terukur.")
    
    add_body_p(doc,
        "Tujuan utama dari pelaksanaan proses analisis risiko kuantitatif meliputi:")
    add_num_p(doc, "Mengukur Tingkat Probabilitas Tercapainya Target Proyek: Memberikan estimasi probabilistik objektif mengenai seberapa besar kemungkinan proyek dapat selesai tepat waktu dan sesuai anggaran yang direncanakan (misalnya: probabilitas 78% proyek selesai sebelum 30 Desember).", 1)
    add_num_p(doc, "Menghitung Besaran Cadangan Kontingensi yang Akurat (Contingency Reserves): Menentukan besaran cadangan biaya dan waktu penyangga (contingency buffer) yang rasional berbasis data probabilistik kuantitatif guna menyerap dampak risiko teridentifikasi, bukan sekadar menebak angka persentase.", 2)
    add_num_p(doc, "Mengidentifikasi Risiko yang Paling Berpengaruh terhadap Keseluruhan Proyek (Critical Drivers): Menentukan risiko individu mana yang memberikan kontribusi variabilitas terbesar terhadap deviasi biaya dan jadwal proyek secara global (biasanya divisualisasikan melalui Diagram Tornado).", 3)
    add_num_p(doc, "Mendukung Pengambilan Keputusan Strategis Berbasis Risiko: Membantu eksekutif, sponsor, dan manajer proyek memilih strategi arsitektur sistem atau pemilihan alternatif vendor terbaik berdasarkan analisis nilai ekspektasi moneter (EMV).", 4)

    # =========================================================================
    # SOAL 2
    # =========================================================================
    add_heading_2(doc, "2. Sebutkan dan jelaskan tiga teknik analisis risiko kuantitatif yang umum digunakan (EMV, Decision Tree, Monte Carlo Simulation)!")
    add_body_p(doc,
        "Berdasarkan standar PMBOK® Guide (PMI, 2017), terdapat tiga teknik pemodelan kuantitatif utama yang lazim diterapkan "
        "dalam mengevaluasi risiko proyek:")

    headers_q2 = ["Teknik Kuantitatif", "Definisi & Konsep Dasar", "Mekanisme Kerja Operasional", "Kelebihan & Kapan Paling Tepat Digunakan"]
    data_q2 = [
        [
            "1. Expected Monetary Value (EMV)\n(Nilai Moneter yang Diharapkan)",
            "Konsep statistik yang menghitung hasil moneter rata-rata di masa depan ketika masa depan tersebut memuat skenario yang mungkin atau tidak mungkin terjadi.",
            "Mengalikan nilai probabilitas keterjadian setiap peristiwa dengan dampak moneternya (EMV = P × I), lalu menjumlahkan seluruh nilai untuk mendapatkan nilai ekspektasi bersih.",
            "• Sangat sederhana, cepat, dan mudah dipahami manajemen\n• Tepat digunakan untuk menghitung cadangan kontingensi dan mengevaluasi portofolio risiko individu."
        ],
        [
            "2. Decision Tree Analysis\n(Analisis Pohon Keputusan)",
            "Alat diagramatis terstruktur yang memodelkan titik keputusan strategis di bawah kondisi ketidakpastian beberapa alternatif tindakan yang bercabang.",
            "Menggunakan simpul keputusan (kotak), simpul peluang/probabilitas (lingkaran), dan cabang hasil akhir (segitiga). Menghitung EMV setiap cabang dari kanan ke kiri (backward fold-back) untuk memilih opsi optimal.",
            "• Memvisualisasikan trade-off antar-alternatif secara eksplisit\n• Tepat digunakan saat memilih teknologi, keputusan Make-or-Buy, atau pemilihan alternatif vendor."
        ],
        [
            "3. Monte Carlo Simulation\n(Simulasi Monte Carlo)",
            "Teknik pemodelan komputasi yang melakukan iterasi perhitungan ribuan kali secara acak menggunakan distribusi probabilitas (Triangular, Beta, Normal) dari variabel input biaya dan jadwal.",
            "Komputer menjalankan simulasi proyek berulang kali (misal: 10.000 iterasi) untuk menghasilkan kurva distribusi kumulatif (S-curve) yang menunjukkan probabilitas penyelesaian proyek pada berbagai target biaya/jadwal.",
            "• Memberikan gambaran ketidakpastian paling komprehensif tanpa menyederhanakan korelasi antar-tugas\n• Tepat untuk proyek berskala besar, kompleks, dan berbiaya tinggi."
        ]
    ]
    create_table(doc, headers_q2, data_q2)

    # =========================================================================
    # SOAL 3
    # =========================================================================
    add_heading_2(doc, "3. Bagaimana cara menghitung Expected Monetary Value (EMV)? Tuliskan rumusnya dan jelaskan dengan contoh sederhana!")
    add_body_p(doc,
        "Expected Monetary Value (EMV) dihitung dengan mengalikan probabilitas terjadinya suatu peristiwa risiko (Probability) "
        "dengan nilai dampak moneter yang ditimbulkannya jika peristiwa tersebut benar-benar terjadi (Impact in Currency). "
        "Formulasi fundamental perhitungan EMV dinyatakan sebagai:")

    # Box formula
    p_box = doc.add_paragraph()
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_box.paragraph_format.space_before = Pt(4)
    p_box.paragraph_format.space_after = Pt(8)
    p_box.paragraph_format.line_spacing = 1.15
    r_box = p_box.add_run("EMV = Probability (P) × Impact (I)")
    r_box.font.name = "Times New Roman"
    r_box.font.size = Pt(13)
    r_box.font.bold = True

    add_body_p(doc,
        "Untuk sebuah proyek yang menghadapi sejumlah n peristiwa risiko independen, total EMV proyek dihitung dengan menjumlahkan "
        "EMV dari setiap peristiwa risiko: Total EMV = Σ (Pi × Ii).")

    add_body_p(doc,
        "Contoh Ilustrasi Sederhana:\n"
        "Sebuah proyek implementasi modul perangkat lunak menghadapi risiko ancaman kerusakan server basis data dengan probabilitas "
        "terjadi P = 20% (0.20). Jika server tersebut rusak, biaya perbaikan dan pemulihan data yang harus ditanggung proyek adalah "
        "sebesar Rp 50.000.000 (bernilai negatif karena merupakan pengeluaran kerugian/ancaman, I = -Rp 50.000.000).\n"
        "Perhitungan EMV:\n"
        "EMV = 0.20 × (-Rp 50.000.000) = -Rp 10.000.000.\n"
        "Artinya, secara statistik ekspektasi kerugian terbobot dari risiko kerusakan server tersebut bernilai Rp 10.000.000. "
        "Angka ini menjadi dasar bagi Manajer Proyek untuk mencadangkan dana kontingensi sebesar Rp 10.000.000 dalam anggaran proyek.")

    # =========================================================================
    # SOAL 4
    # =========================================================================
    add_heading_2(doc, "4. Mengapa EMV untuk peluang dinyatakan sebagai nilai positif dan EMV untuk ancaman dinyatakan sebagai nilai negatif?")
    add_body_p(doc,
        "Dalam kaidah akuntansi keuangan dan manajemen risiko proyek (PMI, 2017), penetapan konvensi tanda matematis pada EMV "
        "mencerminkan arah aliran kas (cash flow) serta dampak ekonomis terhadap anggaran proyek (baseline budget):")

    add_num_p(doc, "EMV Peluang Bertanda Positif (+): Risiko positif atau peluang (opportunity) adalah peristiwa yang mendatangkan keuntungan finansial, efisiensi kerja, atau penghematan biaya bagi proyek. Karena peluang menambah nilai moneter atau mengurangi pengeluaran kas yang semestinya dikeluarkan, dampaknya diperlakukan sebagai arus kas masuk (cash inflow) atau penghematan yang menguntungkan margin proyek, sehingga dikalikan dengan tanda positif (+).", 1)
    add_num_p(doc, "EMV Ancaman Bertanda Negatif (-): Risiko negatif atau ancaman (threat) adalah peristiwa yang menimbulkan kerugian, denda keterlambatan, biaya perbaikan cacat, atau lonjakan pengeluaran sumber daya. Karena ancaman menggerus margin anggaran proyek dan bertindak sebagai arus kas keluar tambahan (cash outflow), dampaknya diperlakukan sebagai biaya kerugian yang merugikan baseline, sehingga diberi tanda negatif (-).", 2)
    add_num_p(doc, "Memungkinkan Penjumlahan Aljabar Portofolio Risiko Bersih (Net Project Exposure): Dengan membedakan tanda positif dan negatif, Manajer Proyek dapat melakukan penjumlahan aljabar langsung terhadap seluruh risiko dalam Risk Register. Total Net EMV = Σ EMV Peluang (+) + Σ EMV Ancaman (-). Hal ini menunjukkan nilai bersih eksposur moneter proyek: peluang dapat secara realistis mengompensasi (meng-offset) sebagian kebutuhan cadangan dana kontingensi untuk ancaman.", 3)

    # =========================================================================
    # SOAL 5
    # =========================================================================
    add_heading_2(doc, "5. Sebutkan dan jelaskan lima strategi respons untuk risiko negatif (ancaman)! Untuk risiko dengan prioritas apa masing-masing strategi paling sesuai digunakan?")
    add_body_p(doc,
        "PMBOK® Guide 6th Edition (PMI, 2017, hal. 441–444) menetapkan lima strategi formal untuk menangani risiko negatif (ancaman), "
        "di mana setiap strategi disesuaikan secara proporsional dengan tingkat keparahan risiko:")

    headers_q5 = ["Strategi Respons Ancaman", "Mekanisme Tindakan & Karakteristik", "Prioritas Risiko yang Paling Sesuai", "Contoh Penerapan Nyata Proyek"]
    data_q5 = [
        [
            "1. Avoid\n(Menghindari)",
            "Mengubah rencana manajemen proyek untuk mengeliminasi ancaman sepenuhnya, mengisolasi sasaran proyek dari dampak risiko, atau membatalkan aktivitas berbahaya.",
            "Prioritas Tinggi / Kritis (Dampak fatal dan probabilitas tinggi yang dapat menggagalkan proyek).",
            "Membatalkan penggunaan pustaka machine learning eksperimental yang tidak stabil dan beralih ke framework stabil Scikit-Learn/XGBoost standar industri."
        ],
        [
            "2. Mitigate\n(Memitigasi / Mengurangi)",
            "Mengambil tindakan preventif proaktif untuk mereduksi probabilitas keterjadian risiko dan/atau mengurangi besarnya dampak hingga berada dalam batas toleransi yang dapat diterima.",
            "Prioritas Tinggi hingga Sedang (Ancaman serius yang tidak dapat dihindari sepenuhnya namun dampaknya dapat ditekan).",
            "Menerapkan kuantisasi model int8 dan arsitektur caching untuk mereduksi latensi inferensi API prediksi keterlambatan PRE-02 agar tidak melampaui SLA."
        ],
        [
            "3. Transfer\n(Mengalihkan / Mentransfer)",
            "Mengalihkan kepemilikan dan dampak finansial risiko kepada pihak ketiga, biasanya disertai pembayaran premi risiko.",
            "Prioritas Tinggi hingga Sedang dengan Dampak Finansial Besar (Risiko spesialisasi yang lebih mampu ditangani pihak eksternal).",
            "Menyewa infrastruktur cloud komputasi bergaransi SLA 99.9% (seperti AWS/GCP) atau membeli polis asuransi peralatan server."
        ],
        [
            "4. Escalate\n(Mengeskalasi)",
            "Menaikkan penanganan risiko ke tingkat manajemen program, portofolio, atau pimpinan organisasi karena ancaman berada di luar wewenang atau ruang lingkup Manajer Proyek.",
            "Prioritas Lintas Batas Organisasi (Risiko strategis, legalitas korporat, atau kebijakan institusi).",
            "Mengeskalasikan pemotongan anggaran lisensi komputasi laboratorium kampus kepada Ketua Program Studi atau Dekan Fakultas."
        ],
        [
            "5. Accept\n(Menerima)",
            "Mengakui keberadaan ancaman tanpa mengambil tindakan proaktif awal. Dapat berupa penerimaan pasif (hanya mencatat di watch list) atau penerimaan aktif (menyusun rencana kontingensi jika risiko terjadi).",
            "Prioritas Rendah (Risiko dengan dampak/probabilitas kecil atau jika biaya mitigasi jauh lebih mahal daripada dampak risiko itu sendiri).",
            "Menerima risiko pemadaman listrik singkat di laboratorium kampus dengan menyiapkan backup baterai UPS (penerimaan aktif)."
        ]
    ]
    create_table(doc, headers_q5, data_q5)

    # =========================================================================
    # SOAL 6
    # =========================================================================
    add_heading_2(doc, "6. Sebutkan dan jelaskan empat strategi respons untuk risiko positif (peluang)!")
    add_body_p(doc,
        "Untuk memaksimalkan manfaat dari peristiwa menguntungkan yang tidak pasti, PMI (2017, hal. 444–446) "
        "merumuskan empat strategi respons untuk risiko positif (peluang):")

    headers_q6 = ["Strategi Respons Peluang", "Definisi & Mekanisme Kerja", "Tujuan Utama", "Contoh Penerapan Nyata Proyek PRE-02"]
    data_q6 = [
        [
            "1. Exploit\n(Mengeksploitasi)",
            "Mengambil tindakan proaktif untuk memastikan bahwa ketidakpastian dihilangkan dan peluang 100% pasti terwujud.",
            "Membuat probabilitas keterjadian menjadi 1.0 (pasti terjadi).",
            "Menugaskan Lead Data Scientist terbaik secara penuh untuk langsung mengintegrasikan pustaka ONNX Runtime begitu rilis resmi keluar, memastikan model terakselerasi maksimal."
        ],
        [
            "2. Enhance\n(Meningkatkan)",
            "Mengambil langkah untuk meningkatkan probabilitas keterjadian dan/atau memperbesar dampak positif dari peluang yang ada.",
            "Mendorong faktor pemicu peluang agar potensi manfaat melonjak.",
            "Menambah alokasi waktu ekstraksi fitur otomatis pada dataset agar daya diskriminasi model (skor AUC-ROC) meningkat dari 0.82 menjadi 0.88."
        ],
        [
            "3. Share\n(Berbagi)",
            "Mengalihkan kepemilikan peluang sebagian atau seluruhnya kepada pihak ketiga (mitra/vendor) yang memiliki keahlian lebih baik dalam menangkap peluang.",
            "Menciptakan sinergi win-win solution yang memaksimalkan pembagian keuntungan.",
            "Bekerja sama dengan tim pengembang UI/UX eksternal untuk bersama-sama memanfaatkan peluang pameran kompetisi inovasi aplikasi manajemen proyek."
        ],
        [
            "4. Accept\n(Menerima)",
            "Mengakui adanya peluang yang menguntungkan namun tidak mengambil tindakan aktif terencana untuk mengejarnya; bersedia memanfaatkannya jika terjadi secara alami.",
            "Menghemat sumber daya tanpa melakukan investasi biaya ekstra.",
            "Mengetahui adanya peluang beasiswa riset tambahan dari kementerian, namun tim memilih fokus menuntaskan baseline tanpa mengerahkan waktu untuk membuat proposal tambahan."
        ]
    ]
    create_table(doc, headers_q6, data_q6)

    # =========================================================================
    # SOAL 7
    # =========================================================================
    add_heading_2(doc, "7. Apa perbedaan antara strategi Avoid dan Mitigate dalam merespons ancaman?")
    add_body_p(doc,
        "Meskipun kedua strategi ini sama-sama ditujukan untuk menangani ancaman serius pada proyek, "
        "terdapat perbedaan mendasar dalam filosofi pendekatan, mekanisme eksekusi, dan kondisi akhir risiko:")

    headers_q7 = ["Dimensi Perbedaan", "Strategi Avoid (Menghindari)", "Strategi Mitigate (Memitigasi / Mengurangi)"]
    data_q7 = [
        [
            "Tujuan terhadap Probabilitas & Dampak",
            "Mengeliminasi ancaman secara total: Membuat probabilitas terjadinya menjadi 0% (P = 0) atau mengisolasi proyek sehingga dampak menjadi nol.",
            "Mereduksi probabilitas dan/atau dampak ke tingkat yang dapat ditoleransi (skor risiko turun ke zona aman yang dapat diterima organisasi)."
        ],
        [
            "Perubahan Rencana Proyek (Project Plan)",
            "Sering kali memerlukan perubahan mendasar pada rencana manajemen proyek: mengubah ruang lingkup, membatalkan fitur, atau mengganti metodologi secara radikal.",
            "Rencana proyek dan sasaran utama tetap dipertahankan, namun ditambahkan aktivitas pencegahan atau proteksi ekstra ke dalam jadwal kerja."
        ],
        [
            "Status Risiko Residu (Residual Risk)",
            "Tidak menyisakan risiko residu terkait peristiwa tersebut karena sumber ancaman telah dihilangkan sepenuhnya.",
            "Masih menyisakan risiko residu (residual risk) dalam kadar rendah yang harus terus dipantau dalam Watch List."
        ],
        [
            "Kapan Strategi Dipilih",
            "Ketika dampak risiko berpotensi menimbulkan kegagalan fatal proyek dan organisasi tidak memiliki toleransi untuk menanggungnya.",
            "Ketika risiko tidak mungkin dihilangkan sepenuhnya karena merupakan bagian inheren dari aktivitas teknis yang tidak dapat dihindari."
        ],
        [
            "Contoh Kasus PRE-02",
            "Avoid: Menghapus modul integrasi telemetri hardware IoT yang sangat rentan kerusakan fisik dari ruang lingkup proyek PRE-02.",
            "Mitigate: Melakukan teknik kuantisasi bobot model dan pruning jaringan untuk mempercepat waktu komputasi inferensi API hingga di bawah 100 ms."
        ]
    ]
    create_table(doc, headers_q7, data_q7)

    # =========================================================================
    # SOAL 8
    # =========================================================================
    add_heading_2(doc, "8. Apa yang dimaksud dengan Contingent Response Strategy dan kapan strategi ini digunakan?")
    add_body_p(doc,
        "Contingent Response Strategy (Strategi Respons Kontinjensi / Fallback Plan) adalah rencana respons risiko yang telah dirancang "
        "sebelumnya, namun hanya akan dieksekusi jika kondisi atau peristiwa pemicu tertentu yang telah didefinisikan (predefined risk triggers) "
        "benar-benar terjadi (PMBOK® Guide 6th Edition, PMI, 2017, hal. 445). Strategi ini juga sering disebut sebagai rencana cadangan (Plan B).")

    add_body_p(doc,
        "Karakteristik Operasional dan Waktu Penerapan Strategi Respons Kontinjensi:")
    add_num_p(doc, "Didorong oleh Indikator Pemicu Terukur (Trigger-Driven): Strategi ini mensyaratkan adanya indikator peringatan dini yang jelas. Misalnya dalam proyek PRE-02: \"Jika deviasi jadwal pada sprint 4 melampaui 7 hari kalender, maka alokasikan komputasi server paralel cadangan\". Ketika pemicu tercapai, respons langsung diaktifkan secara otomatis tanpa perdebatan panjang.", 1)
    add_num_p(doc, "Didukung oleh Cadangan Kontingensi (Contingency Reserves): Rencana kontinjensi membutuhkan alokasi sumber daya biaya dan waktu penyangga (buffer) yang telah dicadangkan dalam baseline anggaran dan jadwal proyek.", 2)
    add_num_p(doc, "Kapan Paling Tepat Digunakan: Strategi ini digunakan ketika tim memilih pendekatan penerimaan aktif (active acceptance) terhadap risiko dengan dampak moderat hingga tinggi, di mana tindakan pencegahan di awal dinilai tidak efisien secara biaya, namun tim tidak boleh membiarkan proyek tanpa rencana aksi saat risiko benar-benar terjadi.", 3)

    # =========================================================================
    # SOAL 9
    # =========================================================================
    add_heading_2(doc, "9. Apa perbedaan antara analisis risiko kualitatif dan analisis risiko kuantitatif? Kapan masing-masing digunakan?")
    add_body_p(doc,
        "Dalam kerangka manajemen risiko proyek, analisis kualitatif dan analisis kuantitatif merupakan dua tahapan evaluasi "
        "yang saling melengkapi namun memiliki perbedaan metodologis yang sangat kontras:")

    headers_q9 = ["Karakteristik Pembanding", "Analisis Risiko Kualitatif (Perform Qualitative)", "Analisis Risiko Kuantitatif (Perform Quantitative)"]
    data_q9 = [
        [
            "Sifat Pendekatan & Metodologi",
            "Subjektif / Deskriptif: Mengandalkan persepsi ahli, penilaian tim, dan skala ordinal (Tinggi, Sedang, Rendah; skala 1–5).",
            "Objektif / Numerik: Mengandalkan matematika probabilitas, simulasi komputasi statistik, dan nilai moneter terkuantisasi (Rp / Jam)."
        ],
        [
            "Output Utama",
            "Peringkat prioritas relatif risiko, pemetaan sel kisi-kisi matriks P&I, dan daftar pantau (Watch List).",
            "Estimasi probabilitas keberhasilan proyek, distribusi biaya/jadwal probabilistik, nilai EMV, dan besaran cadangan kontingensi eksak."
        ],
        [
            "Kebutuhan Waktu & Sumber Daya",
            "Cepat, hemat biaya, dan tidak membutuhkan perangkat lunak pemodelan statistik yang rumit.",
            "Memerlukan waktu lebih lama, data historis yang andal, keahlian statistik khusus, dan tool simulasi (misal: @RISK, Crystal Ball)."
        ],
        [
            "Kapan Digunakan",
            "Wajib dilakukan pada seluruh risiko di setiap proyek, dilaksanakan segera setelah fase identifikasi risiko dan diperbarui berkala.",
            "Dilakukan secara selektif pada risiko-risiko prioritas tinggi yang lolos dari analisis kualitatif, serta pada proyek-proyek bernilai tinggi/kritis."
        ]
    ]
    create_table(doc, headers_q9, data_q9)
