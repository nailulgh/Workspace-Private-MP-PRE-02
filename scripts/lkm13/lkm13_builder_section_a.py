# -*- coding: utf-8 -*-
"""
Section A Builder: Tugas Tertulis Individu
Pertemuan 13: Manajemen Pengadaan & Pemangku Kepentingan Proyek
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
    add_heading_2(doc, "1. Apa yang dimaksud dengan manajemen pengadaan proyek dan mengapa area pengetahuan ini penting?")
    add_body_p(doc,
        "Manajemen Pengadaan Proyek (Project Procurement Management) adalah area pengetahuan manajemen proyek yang mencakup proses-proses "
        "yang diperlukan untuk membeli atau mengakuisisi produk, jasa, atau hasil kerja yang dibutuhkan dari luar tim proyek "
        "(PMBOK® Guide 6th Edition, PMI, 2017, hal. 459–502). Area pengetahuan ini mencakup tata kelola kontrak formal, administrasi hukum, "
        "pengendalian perubahan pesanan, evaluasi vendor penjual (sellers/contractors), serta penutupan perjanjian kerja sama pengadaan.")
    
    add_body_p(doc,
        "Urgensi area pengetahuan manajemen pengadaan terhadap keberhasilan proyek didasari oleh faktor-faktor kritis berikut:")
    add_num_p(doc, "Menjembatani Keterbatasan Kapasitas dan Keahlian Internal: Tidak ada organisasi yang memiliki seluruh sumber daya dan keahlian spesialis yang dibutuhkan untuk menyelesaikan proyek kompleks. Pengadaan memungkinkan proyek mengakuisisi teknologi mutakhir (misal: lisensi komputasi cloud, pustaka model teroptimasi, data telemetri historis) tanpa harus mengembangkannya dari nol.", 1)
    add_num_p(doc, "Efisiensi Biaya dan Pengalihan Risiko Finansial: Pengadaan yang terencana dengan baik membantu organisasi mendapatkan nilai investasi terbaik (best value for money) melalui mekanisme pasar kompetitif. Selain itu, pemilihan jenis kontrak yang tepat memungkinkan pengalihan sebagian risiko biaya dan keterlambatan kepada vendor pihak ketiga.", 2)
    add_num_p(doc, "Kepastian Hukum dan Perlindungan Hubungan Bisnis: Kontrak pengadaan merupakan instrumen hukum yang mengikat (legally binding). Manajemen pengadaan yang ketat melindungi hak-hak proyek, mencegah perselisihan interpretasi deliverables, dan menjamin klausul penalti ditegakkan jika terjadi wanprestasi.", 3)
    add_num_p(doc, "Konteks Relevansi pada Proyek PRE-02: Dalam riset sistem peringatan dini machine learning PRE-02, tim membutuhkan infrastruktur server berkecepatan tinggi dan penyimpanan dataset berskala besar. Pengadaan layanan compute cloud (seperti AWS EC2/GCP AI Platform) memastikan pelatihan model deep learning MLP dan ensemble gradient boosting dapat dieksekusi tanpa kendala keterbatasan hardware lokal kampus.", 4)

    # =========================================================================
    # SOAL 2
    # =========================================================================
    add_heading_2(doc, "2. Sebutkan dan jelaskan tiga proses dalam manajemen pengadaan proyek!")
    add_body_p(doc,
        "Berdasarkan standar PMBOK® Guide 6th Edition (PMI, 2017, Bab 12), manajemen pengadaan proyek disederhanakan "
        "menjadi tiga proses utama yang berurutan dan terintegrasi:")

    headers_q2 = ["Nama Proses", "Kelompok Proses", "Tujuan & Mekanisme Kerja Utama", "Output Kunci"]
    data_q2 = [
        [
            "1. Plan Procurement Management\n(Merencanakan Manajemen Pengadaan)",
            "Planning\n(Perencanaan)",
            "Mendokumentasikan keputusan pengadaan proyek, menentukan pendekatan akuisisi, mengidentifikasi calon penjual potensial, melakukan analisis Make-or-Buy, memilih jenis kontrak yang tepat, serta menyusun kriteria evaluasi penawaran.",
            "• Procurement Management Plan\n• Procurement Strategy\n• Bid Documents (RFP, RFQ, RFI)\n• Procurement Statement of Work (SOW)\n• Make-or-Buy Decisions"
        ],
        [
            "2. Conduct Procurements\n(Melaksanakan Pengadaan)",
            "Executing\n(Pelaksanaan)",
            "Menerbitkan dokumen lelang ke pasar, menerima respons/proposal dari calon penjual, mengevaluasi proposal berdasarkan kriteria terbobot, melakukan negosiasi teknis dan komersial, memilih penjual terbaik, serta menandatangani kontrak hukum resmi.",
            "• Selected Sellers\n• Agreements (Kontrak Hukum)\n• Change Requests\n• Pembaruan Project Management Plan"
        ],
        [
            "3. Control Procurements\n(Mengendalikan Pengadaan)",
            "Monitoring & Controlling\n(Pemantauan & Pengendalian)",
            "Mengelola hubungan kontrak kerja sama, memantau kinerja deliverable vendor terhadap SOW, menyetujui klaim pembayaran dan faktur, mengelola perubahan kontrak, menyelesaikan sengketa, melakukan audit pengadaan, hingga penutupan administratif kontrak.",
            "• Closed Procurements (Penutupan Kontrak)\n• Work Performance Information\n• Procurement Documentation Updates\n• Change Requests"
        ]
    ]
    create_table(doc, headers_q2, data_q2)

    # =========================================================================
    # SOAL 3
    # =========================================================================
    add_heading_2(doc, "3. Sebutkan dan jelaskan perbedaan antara tiga jenis kontrak utama: Fixed Price (FP), Cost Reimbursable (CR), dan Time and Material (T&M)! Berikan contoh penggunaan masing-masing jenis kontrak!")
    add_body_p(doc,
        "Kontrak pengadaan dikelompokkan ke dalam tiga kategori utama berdasarkan mekanisme penetapan harga, cara pembayaran, "
        "dan pembagian risiko finansial antara pembeli (buyer) dan penjual (seller) (PMI, 2017):")

    headers_q3 = ["Kategori Kontrak", "Mekanisme Pembayaran & Karakteristik", "Distribusi Risiko Finansial", "Variasi Jenis Kontrak", "Contoh Penerapan Nyata dalam Proyek TI"]
    data_q3 = [
        [
            "1. Fixed Price (FP)\n(Harga Tetap)",
            "Pembeli membayar sejumlah harga tetap yang telah disepakati untuk paket pekerjaan atau produk tertentu, terlepas dari berapa biaya riil yang dikeluarkan penjual.",
            "Risiko biaya berada penuh pada PENJUAL (Seller). Jika terjadi pembengkakan biaya produksi, penjual menanggung kerugian.",
            "• Firm Fixed Price (FFP)\n• Fixed Price Incentive Fee (FPIF)\n• Fixed Price with EPA (FP-EPA)",
            "Pengadaan lisensi server basis data komersial tahunan seharga Rp 25.000.000 tetap, atau pengadaan pembuatan modul login API dengan spesifikasi teknis yang sudah 100% final dan beku."
        ],
        [
            "2. Cost Reimbursable (CR)\n(Penggantian Biaya Riil)",
            "Pembeli mengganti seluruh biaya aktual sah yang dikeluarkan penjual untuk menyelesaikan pekerjaan, ditambah biaya keuntungan (fee) bagi penjual.",
            "Risiko biaya berada penuh pada PEMBELI (Buyer). Jika terjadi pembengkakan biaya, pembeli wajib mengganti seluruh pengeluaran.",
            "• Cost Plus Fixed Fee (CPFF)\n• Cost Plus Incentive Fee (CPIF)\n• Cost Plus Award Fee (CPAF)",
            "Kontrak riset eksperimental pembuatan model deep learning generasi baru di mana algoritma dan waktu konvergensi belum diketahui secara pasti, sehingga biaya GPU komputasi riil diganti pembeli plus fee 10%."
        ],
        [
            "3. Time and Material (T&M)\n(Waktu dan Material)",
            "Kombinasi hibrida antara FP dan CR di mana pembeli membayar berdasarkan tarif satuan waktu kerja per jam/hari (labor rate) ditambah biaya aktual material yang digunakan.",
            "Risiko dibagi BERSAMA (Pembeli menanggung risiko lonjakan jam kerja, Penjual menanggung risiko ketersediaan staf).",
            "Sering kali dilengkapi klausul batas atas Not-To-Exceed (NTE) untuk membatasi pengeluaran maksimal pembeli.",
            "Menyewa jasa konsultan Senior MLOps Specialist selama 40 jam kerja dengan tarif Rp 500.000/jam untuk membantu konfigurasi deployment model PRE-02 ke server Kubernetes."
        ]
    ]
    create_table(doc, headers_q3, data_q3)

    # =========================================================================
    # SOAL 4
    # =========================================================================
    add_heading_2(doc, "4. Dalam situasi apa kontrak Fixed Price lebih disarankan dibandingkan Cost Reimbursable, dan sebaliknya? Jelaskan dengan mempertimbangkan faktor ruang lingkup dan risiko!")
    add_body_p(doc,
        "Pemilihan jenis kontrak yang tepat merupakan keputusan strategis yang ditentukan oleh dua parameter utama: "
        "tingkat kejelasan ruang lingkup pekerjaan (scope definition) dan toleransi profil risiko yang siap ditanggung organisasi (risk allocation):")

    add_heading_3(doc, "a. Situasi di Mana Kontrak Fixed Price (FP) Lebih Disarankan:")
    add_bullet_p(doc, "Ruang Lingkup Sangat Jelas dan Terdefinisi dengan Baik (Well-Defined Scope): Pekerjaan memiliki spesifikasi teknis, Procurement Statement of Work (SOW), dan kriteria penerimaan yang mendetail, stabil, serta tidak akan mengalami perubahan signifikan. Penjual dapat menghitung estimasi biaya secara akurat.")
    add_bullet_p(doc, "Pembeli Ingin Kepastian Anggaran Maksimal: Ketika pembeli memiliki pagu anggaran yang ketat dan tidak memiliki toleransi terhadap pembengkakan biaya (cost predictability is paramount).")
    add_bullet_p(doc, "Transfer Risiko Biaya ke Penjual: Pembeli ingin mengalihkan risiko ketidakefisienan operasional kepada penjual. Penjual dipaksa bekerja efisien karena setiap pemborosan akan langsung menggerus margin labanya.")

    add_heading_3(doc, "b. Situasi di Mana Kontrak Cost Reimbursable (CR) Lebih Disarankan:")
    add_bullet_p(doc, "Ruang Lingkup Belum Jelas atau Bersifat Eksploratif/Riset (Evolving / High-Uncertainty Scope): Pada proyek inovasi teknologi, riset Machine Learning, atau pengembangan software adaptif di mana arsitektur akhir dan tantangan teknis belum diketahui secara pasti. Jika dipaksakan menggunakan Fixed Price, penjual akan memasukkan margin kontingensi risiko yang sangat tinggi (inflasi harga) atau menolak mengajukan penawaran.")
    add_bullet_p(doc, "Kebutuhan Memulai Pekerjaan Secara Cepat (High Urgency): Waktu tidak mencukupi untuk menyusun dokumen spesifikasi detail sebelum kontrak ditandatangani. Pembeli dapat segera menginstruksikan penjual bekerja sementara ruang lingkup disempurnakan secara paralel.")
    add_bullet_p(doc, "Fleksibilitas Pengendalian Mutu: Pembeli mempertahankan kendali penuh terhadap arah teknis pekerjaan dan berhak mengubah prioritas tanpa harus menegosiasikan change order formal yang berlarut-larut.")

    # =========================================================================
    # SOAL 5
    # =========================================================================
    add_heading_2(doc, "5. Apa yang dimaksud dengan analisis make-or-buy dan mengapa analisis ini penting dalam perencanaan pengadaan?")
    add_body_p(doc,
        "Analisis Make-or-Buy (Make-or-Buy Analysis) adalah teknik manajemen analitis yang digunakan pada proses Plan Procurement Management "
        "untuk mengevaluasi dan memutuskan apakah suatu produk, modul perangkat lunak, aset, atau layanan pekerjaan sebaiknya diproduksi "
        "secara mandiri di internal tim proyek (Make) atau dibeli/dialihdayakan dari vendor eksternal (Buy) (PMI, 2017, hal. 479).")
    
    add_body_p(doc,
        "Analisis ini melibatkan perbandingan kuantitatif (analisis biaya langsung, biaya tidak langsung, biaya modal, dan biaya operasional) "
        "serta pertimbangan kualitatif strategis. Urgensi pentingnya analisis Make-or-Buy meliputi:")
    
    add_num_p(doc, "Optimalisasi Alokasi Sumber Daya Finansial dan Titik Impas (Break-Even Analysis): Membantu proyek menghitung volume penggunaan di mana opsi Buy menjadi lebih murah daripada Make, atau sebaliknya, sehingga mencegah investasi modal (capital expenditure) yang sia-sia pada kapabilitas yang jarang digunakan.", 1)
    add_num_p(doc, "Fokus pada Kompetensi Inti Proyek (Core Competencies): Memastikan tim internal memusatkan waktu dan keahlian terbaiknya pada aktivitas diferensiasi utama proyek (misal: inovasi algoritma kalibrasi model PRE-02), sementara modul pendukung komoditas (seperti antarmuka otentikasi login pengguna) dialihdayakan ke penyedia spesialis.", 2)
    add_num_p(doc, "Pertimbangan Ketersediaan Kapasitas dan Waktu Pasar (Time-to-Market): Jika tim internal mengalami kelebihan beban kerja (over-allocated) dan tenggat waktu rilis mendesak, opsi Buy memungkinkan integrasi instan yang memangkas jadwal pengembangan secara signifikan.", 3)
    add_num_p(doc, "Perlindungan Kekayaan Intelektual dan Kendali Kualitas: Analisis ini mempertimbangkan risiko keamanan; data rahasia atau algoritma proprietari bernilai tinggi umumnya diputuskan Make untuk mencegah kebocoran informasi kepada pihak ketiga.", 4)

    # =========================================================================
    # SOAL 6
    # =========================================================================
    add_heading_2(doc, "6. Sebutkan dan jelaskan empat proses dalam manajemen pemangku kepentingan proyek!")
    add_body_p(doc,
        "Manajemen Pemangku Kepentingan Proyek (Project Stakeholder Management) mencakup empat proses yang dirancang "
        "untuk mengidentifikasi pihak-pihak berkepentingan, menganalisis ekspektasi mereka, dan melibatkan mereka secara efektif "
        "(PMBOK® Guide 6th Edition, PMI, 2017, Bab 13, hal. 503–536):")

    headers_q6 = ["Nama Proses", "Kelompok Proses", "Definisi, Tujuan, dan Mekanisme Kerja", "Output Kunci"]
    data_q6 = [
        [
            "1. Identify Stakeholders\n(Mengidentifikasi Pemangku Kepentingan)",
            "Initiating\n(Inisiasi)",
            "Mengidentifikasi seluruh individu, kelompok, atau organisasi yang memengaruhi atau terpengaruh oleh keputusan, aktivitas, atau hasil proyek secara teratur, serta mendokumentasikan peran, ekspektasi, dan tingkat pengaruh mereka.",
            "• Stakeholder Register\n• Change Requests\n• Pembaruan Project Management Plan"
        ],
        [
            "2. Plan Stakeholder Engagement\n(Merencanakan Keterlibatan)",
            "Planning\n(Perencanaan)",
            "Mengembangkan pendekatan strategis untuk melibatkan para pemangku kepentingan berdasarkan analisis kebutuhan, kepentingan personal, dan potensi dampak mereka terhadap keberhasilan proyek guna memenangkan dukungan mereka.",
            "• Stakeholder Engagement Plan\n• Pembaruan Project Management Plan"
        ],
        [
            "3. Manage Stakeholder Engagement\n(Mengelola Keterlibatan)",
            "Executing\n(Pelaksanaan)",
            "Berkomunikasi aktif dan bekerja sama secara nyata dengan pemangku kepentingan untuk memenuhi kebutuhan dan ekspektasi mereka, menangani isu dan resistensi segera, serta membina kolaborasi positif sepanjang proyek.",
            "• Change Requests\n• Issue Log (Log Masalah)\n• Pembaruan Stakeholder Register\n• Project Communications"
        ],
        [
            "4. Monitor Stakeholder Engagement\n(Memantau Keterlibatan)",
            "Monitoring & Controlling\n(Pemantauan & Pengendalian)",
            "Memantau hubungan interpersonal dan efektivitas interaksi pemangku kepentingan secara menyeluruh, serta menyesuaikan strategi dan rencana keterlibatan jika terjadi perubahan dinamika kekuasaan atau pergeseran persepsi.",
            "• Work Performance Information\n• Change Requests\n• Pembaruan Stakeholder Engagement Plan\n• Pembaruan Stakeholder Register"
        ]
    ]
    create_table(doc, headers_q6, data_q6)

    # =========================================================================
    # SOAL 7
    # =========================================================================
    add_heading_2(doc, "7. Apa yang dimaksud dengan Stakeholder Register dan informasi apa saja yang harus dicatat di dalamnya?")
    add_body_p(doc,
        "Stakeholder Register (Daftar Pemangku Kepentingan) adalah dokumen manajemen proyek sentral yang berfungsi mencatat "
        "seluruh informasi relevan mengenai setiap pihak yang teridentifikasi memiliki kepentingan atau pengaruh terhadap proyek "
        "(PMI, 2017, hal. 514). Dokumen ini menjadi masukan (input) krusial dalam perencanaan komunikasi, manajemen risiko, dan penentuan ruang lingkup.")
    
    add_body_p(doc,
        "Komponen informasi komprehensif yang wajib dicatat di dalam Stakeholder Register dikelompokkan ke dalam tiga kategori utama:")
    
    add_num_p(doc, "Informasi Identifikasi (Identification Information): Nama lengkap pemangku kepentingan, posisi/jabatan organisasi, departemen/perusahaan asal, peran spesifik dalam proyek (misal: Sponsor, Project Manager, Lead Data Scientist, Klien), lokasi kerja, dan kontak resmi (email, telepon).", 1)
    add_num_p(doc, "Informasi Penilaian (Assessment Information): Ekspektasi dan kebutuhan utama terhadap hasil akhir proyek, potensi dampak keterlibatan mereka terhadap deliverables, fase siklus hidup proyek di mana pemangku kepentingan memiliki minat tertinggi, serta klasifikasi tingkat Kekuasaan (Power) dan Kepentingan (Interest).", 2)
    add_num_p(doc, "Klasifikasi Pemangku Kepentingan (Stakeholder Classification): Kategori posisi pemangku kepentingan berdasarkan batas organisasi (Internal vs Eksternal), orientasi sikap terhadap proyek (Pendukung/Supporter, Netral/Neutral, Penentang/Resistant, atau Pemimpin/Leading), serta penempatan kuadran dalam Power/Interest Grid.", 3)

    # =========================================================================
    # SOAL 8
    # =========================================================================
    add_heading_2(doc, "8. Jelaskan apa yang dimaksud dengan Power/Interest Grid dan bagaimana alat ini digunakan untuk menentukan strategi keterlibatan pemangku kepentingan!")
    add_body_p(doc,
        "Power/Interest Grid (Kisi Kekuasaan/Kepentingan / Matriks Mendelow, 1981) adalah alat visual dan analitis klasifikasi "
        "yang memetakan pemangku kepentingan ke dalam matriks dua dimensi berdasarkan kombinasi dua atribut kritis:")
    
    add_bullet_p(doc, "Tingkat Kekuasaan / Pengaruh (Power / Authority): Besarnya otoritas, wewenang hierarkis, atau kemampuan formal yang dimiliki pemangku kepentingan untuk menghentikan, mengubah arah, mengalokasikan anggaran, atau memengaruhi hasil akhir proyek.")
    add_bullet_p(doc, "Tingkat Kepentingan (Interest / Concern): Seberapa besar perhatian, kebutuhan, kepedulian, atau konsekuensi yang akan diterima pemangku kepentingan akibat keberhasilan atau kegagalan proyek.")

    add_body_p(doc,
        "Pemanfaatan Alat untuk Menentukan Strategi Keterlibatan:\n"
        "Matriks membagi lanskap pemangku kepentingan ke dalam empat kuadran terpisah yang secara langsung memandu penetapan "
        "tingkat intensitas komunikasi dan pendekatan hubungan kerja:")
    add_num_p(doc, "Kuadran 1: Power Tinggi, Interest Tinggi -> Strategi \"Manage Closely\" (Kelola Secara Ketat).", 1)
    add_num_p(doc, "Kuadran 2: Power Tinggi, Interest Rendah -> Strategi \"Keep Satisfied\" (Jaga Tetap Puas).", 2)
    add_num_p(doc, "Kuadran 3: Power Rendah, Interest Tinggi -> Strategi \"Keep Informed\" (Jaga Tetap Terinformasi).", 3)
    add_num_p(doc, "Kuadran 4: Power Rendah, Interest Rendah -> Strategi \"Monitor\" (Pantau dengan Upaya Minimal).", 4)
    add_body_p(doc,
        "Alat ini memastikan Manajer Proyek tidak membuang-buang waktu berkomunikasi berlebihan pada pihak berdaya rendah, "
        "serta tidak mengabaikan pihak berkekuasaan tinggi yang berpotensi mematikan proyek.")

    # =========================================================================
    # SOAL 9
    # =========================================================================
    add_heading_2(doc, "9. Bagaimana strategi komunikasi yang berbeda untuk setiap kuadran dalam Power/Interest Grid? Jelaskan!")
    add_body_p(doc,
        "Setiap kuadran dalam Power/Interest Grid menuntut pendekatan komunikasi yang sangat spesifik dan terukur "
        "guna menjaga keselarasan ekspektasi dan efisiensi waktu kerja (PMI, 2017):")

    headers_q9 = ["Kuadran & Karakteristik", "Strategi Keterlibatan", "Saluran & Metode Komunikasi", "Frekuensi Komunikasi", "Contoh Stakeholder Proyek (PRE-02)"]
    data_q9 = [
        [
            "Kuadran I:\nPower Tinggi,\nInterest Tinggi",
            "Manage Closely\n(Kelola Sangat Dekat & Intensif)",
            "• Rapat koordinasi tatap muka langsung / telekonferensi rutin\n• Pelibatan aktif dalam pengambilan keputusan strategis arsitektur\n• Laporan status mendalam (executive summary & detail milestone)",
            "Tinggi\n(Mingguan atau sesuai milestone kritis)",
            "• Dosen Pengampu Mata Kuliah (Dr. M. Ainul Yaqin)\n• Project Manager\n• Lead Data Scientist & Lead Software Engineer"
        ],
        [
            "Kuadran II:\nPower Tinggi,\nInterest Rendah",
            "Keep Satisfied\n(Jaga Tetap Puas & Jangan Diganggu Detail Teknis)",
            "• Laporan ringkasan tingkat tinggi (high-level dashboard)\n• Komunikasi formal berkala dan memo resmi\n• Respon cepat terhadap pertanyaan tanpa membebani mereka dengan perdebatan operasional harian",
            "Moderat\n(Bulanan atau saat perubahan baseline anggaran)",
            "• Ketua Program Studi Teknik Informatika\n• Pimpinan Fakultas Sains dan Teknologi\n• Administrator Server Kampus / Kepala Lab Komputasi"
        ],
        [
            "Kuadran III:\nPower Rendah,\nInterest Tinggi",
            "Keep Informed\n(Jaga Selalu Terinformasi & Dengarkan Masukan)",
            "• Buletin berkala, repositori dokumentasi terbuka (GitHub Wiki)\n• Sesi demonstrasi sistem (showcase demo) dan kuesioner pengguna\n• Kanal komunikasi asinkron (Discord channel / email update)",
            "Sedang hingga Rutin\n(Bi-weekly atau saat rilis prototipe antarmuka)",
            "• Calon Pengguna Akhir (Manajer Proyek IT luar)\n• Mahasiswa anggota tim riset paralel\n• Asisten Laboratorium Komputasi"
        ],
        [
            "Kuadran IV:\nPower Rendah,\nInterest Rendah",
            "Monitor\n(Pantau Pasif dengan Upaya Minimal)",
            "• Akses informasi mandiri melalui metode Pull Communication (portal web repositori proyek)\n• Tidak memerlukan komunikasi dorong (push) aktif harian",
            "Rendah / Sesuai Kebutuhan\n(Hanya saat terjadi perubahan kebijakan besar)",
            "• Vendor penyedia lisensi perangkat lunak umum\n• Komunitas mahasiswa umum di luar proyek"
        ]
    ]
    create_table(doc, headers_q9, data_q9)
